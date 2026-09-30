"""Speaker Context Vector S(t) — v1.1.0 extension to CANONICAL v1.0.0.

S(t) = v_lock (32) ⊕ φ_semantic (384) ⊕ φ_declared (64) = 480 dims

Channel reconciliation (the v1.1.0 fix):
- φ_semantic MUST come from sentence-transformer embeddings
  (all-MiniLM-L6-v2) of the turn's first-person identity claims.
  If a turn contains no identity claim, the previous value persists.
  It MUST NOT reuse v_mix.
- φ_declared MUST come from NER over declared name/role tokens.
  If no name/role token is declared, it is the null vector.
  It MUST NOT be a truncated v_lock.

Locked constants (paper spec, do not drift):
    THETA_SPEAKER = 0.85   same-speaker cosine threshold
    THETA_NEW     = 0.50   new-speaker cosine threshold
    K_STYLE       = 32     v_lock style channel dims
    K_SEMANTIC    = 384    φ_semantic channel dims (all-MiniLM-L6-v2)
    K_DECLARED    = 64     φ_declared channel dims
    EMA_MU        = 0.02   S_stored EMA rate (~35-turn half-life)
"""
import hashlib
import re

import numpy as np

THETA_SPEAKER = 0.85
THETA_NEW = 0.50
K_STYLE = 32
K_SEMANTIC = 384
K_DECLARED = 64
EMA_MU = 0.02

_SENTENCE_MODEL_NAME = "all-MiniLM-L6-v2"

# First-person identity claim patterns (English + Hinglish anchors).
_IDENTITY_CLAIM_RE = re.compile(
    r"\b(i am|i'm|im\b|my name is|it's me|its me|it is me|this is|"
    r"call me|main\b[^\n.!?]*\bhoon|mera naam)\b",
    re.IGNORECASE,
)

# Role declaration patterns, e.g. "I am a researcher", "my role is lead".
_ROLE_RE = re.compile(
    r"\b(?:i am|i'm|my role is|i work as|i serve as)\s+(?:a|an|the)?\s*"
    r"([a-z][a-z\- ]{2,30})",
    re.IGNORECASE,
)

# Tokens that are capitalised but are not declared names.
_DECLARED_STOPLIST = {
    "I", "The", "This", "That", "It", "Its", "He", "She", "They", "We",
    "You", "Hey", "Hi", "Hello", "Yes", "No", "Ok", "Okay", "Was", "Is",
    "Are", "Am", "Me", "My", "Here", "There", "Main",
}

try:  # spaCy NER is preferred; regex fallback keeps the channel deterministic.
    import spacy as _spacy
    try:
        _NLP = _spacy.load("en_core_web_sm")
    except Exception:
        _NLP = None
except Exception:
    _NLP = None

_ST_MODEL = None
_ST_FAILED = False

# Persisted φ_semantic across turns (channel state, not global identity).
_PREV_SEMANTIC = np.zeros(K_SEMANTIC, dtype=float)


def _sentence_model():
    """Lazy-load all-MiniLM-L6-v2; None if unavailable."""
    global _ST_MODEL, _ST_FAILED
    if _ST_MODEL is not None or _ST_FAILED:
        return _ST_MODEL
    try:
        from sentence_transformers import SentenceTransformer
        _ST_MODEL = SentenceTransformer(_SENTENCE_MODEL_NAME)
    except Exception:
        _ST_FAILED = True
        _ST_MODEL = None
    return _ST_MODEL


def _hashed_vector(tokens, dims):
    """Deterministic fallback embedding: seeded per-token hashing, averaged."""
    if not tokens:
        return np.zeros(dims, dtype=float)
    acc = np.zeros(dims, dtype=float)
    for tok in tokens:
        seed = int(hashlib.md5(tok.lower().encode("utf-8")).hexdigest()[:8], 16)
        rng = np.random.RandomState(seed)
        acc += rng.standard_normal(dims)
    norm = np.linalg.norm(acc)
    return acc / norm if norm > 0 else acc


def extract_identity_claims(text):
    """Return the clauses of `text` that carry first-person identity claims."""
    claims = []
    for clause in re.split(r"[.!?\n;]+", text):
        if _IDENTITY_CLAIM_RE.search(clause):
            claims.append(clause.strip())
    return [c for c in claims if c]


def extract_declared_tokens(text):
    """NER over declared name/role tokens. Returns (names, roles)."""
    names, roles = [], []
    if _NLP is not None:
        doc = _NLP(text)
        names = [ent.text for ent in doc.ents if ent.label_ in ("PERSON", "ORG")]
    else:
        for tok in re.findall(r"\b[A-Z][A-Za-z]+\b|\b[A-Z]{2,}\b", text):
            if tok not in _DECLARED_STOPLIST and tok.capitalize() not in _DECLARED_STOPLIST:
                names.append(tok)
    roles = [m.group(1).strip() for m in _ROLE_RE.finditer(text)]
    return names, roles


def style_lock(text):
    """v_lock (32-dim): deterministic char-n-gram style signature."""
    trigrams = [text[i:i + 3].lower() for i in range(max(len(text) - 2, 1))]
    return _hashed_vector(trigrams, K_STYLE)


def phi_semantic(text):
    """φ_semantic (384-dim): sentence-transformer embedding of first-person
    identity claims. Persists the previous value if the turn has no claim."""
    global _PREV_SEMANTIC
    claims = extract_identity_claims(text)
    if not claims:
        return _PREV_SEMANTIC.copy()
    model = _sentence_model()
    if model is not None:
        vec = np.asarray(model.encode(claims), dtype=float).mean(axis=0)
        if vec.shape[0] != K_SEMANTIC:
            vec = np.resize(vec, K_SEMANTIC)
    else:  # deterministic fallback when sentence-transformers is unavailable
        tokens = re.findall(r"\b\w+\b", " ".join(claims))
        vec = _hashed_vector(tokens, K_SEMANTIC)
    _PREV_SEMANTIC = vec
    return vec.copy()


def phi_declared(text):
    """φ_declared (64-dim): NER embedding of declared name/role tokens.
    Null vector when the turn declares no name or role."""
    names, roles = extract_declared_tokens(text)
    if not names and not roles:
        return np.zeros(K_DECLARED, dtype=float)
    return _hashed_vector(names + roles, K_DECLARED)


def encode_speaker(text):
    """S(t) = v_lock (32) ⊕ φ_semantic (384) ⊕ φ_declared (64) → (480,)."""
    return np.concatenate([
        style_lock(text),
        phi_semantic(text),
        phi_declared(text),
    ])


def update_stored(S_stored, S_new, mu=EMA_MU):
    """EMA update of the stored speaker vector: ~35-turn half-life at mu=0.02."""
    return (1.0 - mu) * np.asarray(S_stored, dtype=float) + mu * np.asarray(S_new, dtype=float)


def cosine(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(a @ b / denom) if denom > 0 else 0.0


def is_same_speaker(similarity):
    return similarity >= THETA_SPEAKER


def is_new_speaker(similarity):
    return similarity < THETA_NEW
