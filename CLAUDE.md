# CLAUDE.md: Emotional AI Architecture Development Guide

## Project Overview

**Emotional AI Architecture** is a research project implementing a multi-layer conversational AI system for context-aware, mood-responsive interactions. The system integrates emotional state recognition, adaptive response generation, and symbolic memory architecture to enable emotionally coherent, identity-consistent AI responses.

This project is part of the **CCCS Framework** research ecosystem, contributing core implementations of the Emotional Feedback Loop, Tone Engine Layer, and Self-Reference Engine components.

## Core Architectural Vision

### The Three Pillars

#### 1. **Emotional Feedback Loop (EFL)**
Real-time affective state tracking and mood-responsive adaptation that enables the system to recognize and respond to emotional context.

**Mathematical Foundation:**
```
E(t+1) = αE(t) + βF(t) + γP(t)
```
Where:
- `E(t)`: Emotional state at time t
- `F(t)`: External feedback signals
- `P(t)`: Pattern-based predictions from symbolic memory
- `α, β, γ`: Tunable coefficients for emotional momentum, feedback responsiveness, and pattern influence

#### 2. **Symbolic Memory Architecture**
Long-term relational memory encoding emotional patterns through constraint geometry, enabling associative recall and identity-consistent behavior over extended conversations.

Key concepts:
- **Constraint Geometry Encoding**: Represents relationships and emotional patterns as geometric constraints
- **Associative Recall**: Retrieval mechanisms that honor emotional context and relational patterns
- **Pattern Storage**: Long-term persistence of emotional and interactional patterns

#### 3. **Adaptive Response Generation**
Context-aware rendering of persona and tone while maintaining identity consistency across topic shifts and emotional states.

Principles:
- Tonal coherence maintenance across conversation context shifts
- Identity-consistent output that reflects the relational history
- Trauma-informed interaction patterns (validated in real-world counseling context)

## Research Validation

**Voice-Layer Counseling Prototype (April 2026)**
- Successfully integrated ElevenLabs voice API with constraint-geometry-encoded emotional context
- Validated trauma-informed interaction patterns in real counseling scenarios
- Demonstrated sub-5-minute emotional disclosure facilitation
- Maintained tonal coherence across sensitive context transitions

This prototype validates the feasibility of the architectural approach in high-stakes emotional contexts.

## Codebase Structure

### Current State
The project is in the **specification and documentation phase**. Core implementation is planned with the following anticipated structure:

```
emotional-ai-architecture/
├── CLAUDE.md                      # This file
├── README.md                      # Project overview and use cases
├── pyproject.toml                 # Python project configuration
├── requirements.txt               # Dependencies
├── .env.example                   # Environment variables template
│
├── src/
│   ├── emotional_ai/
│   │   ├── __init__.py
│   │   ├── core/                  # Core EFL and memory implementations
│   │   │   ├── emotional_loop.py  # EFL formula and state management
│   │   │   ├── memory/            # Symbolic memory architecture
│   │   │   │   ├── constraint_geometry.py
│   │   │   │   └── associative_recall.py
│   │   │   └── state.py          # System state management
│   │   │
│   │   ├── response/              # Adaptive response generation
│   │   │   ├── persona.py        # Context-aware persona rendering
│   │   │   ├── tone_engine.py    # Tonal coherence maintenance
│   │   │   └── identity.py       # Identity consistency mechanisms
│   │   │
│   │   ├── integration/           # External integrations
│   │   │   ├── llm_provider.py   # OpenAI, Claude, Gemini abstractions
│   │   │   ├── voice.py          # ElevenLabs integration
│   │   │   └── memory_store.py   # FAISS, ChromaDB abstractions
│   │   │
│   │   └── utils/
│   │       └── emotional_metrics.py
│   │
│   └── tests/
│       ├── unit/
│       ├── integration/
│       └── research_validation/
│
├── examples/
│   └── counseling_prototype.py    # April 2026 prototype implementation
│
└── docs/
    ├── architecture.md             # Detailed architecture documentation
    ├── research_notes.md          # Research decisions and findings
    └── integration_guide.md       # Integration with CCCS Framework
```

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **LLM Integration** | LangChain, OpenAI SDK, Anthropic SDK |
| **LLM Providers** | OpenAI GPT, Anthropic Claude, Google Gemini |
| **Voice I/O** | ElevenLabs Voice API |
| **Vector Memory** | FAISS, ChromaDB |
| **NLP** | HuggingFace Transformers |
| **API Framework** | FastAPI |
| **Testing** | pytest, hypothesis (property-based testing) |
| **Documentation** | Sphinx |

## Development Workflow

### Git Conventions

#### Branch Naming
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/{feature-name}` - Feature development
- `claude/{feature-description}` - Claude-assisted development
- `research/{topic}` - Research-focused branches

#### Commit Messages
Follow conventional commits format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature implementation
- `fix`: Bug fix
- `research`: Research findings or architectural decisions
- `docs`: Documentation updates
- `refactor`: Code refactoring without behavior change
- `test`: Test additions or modifications
- `ci`: CI/CD configuration

Example:
```
feat(memory): implement constraint geometry encoder

Implements the constraint geometry encoding mechanism for the 
symbolic memory architecture, enabling geometric representation
of emotional relationships. References research papers on 
constraint-based knowledge representation.

Refs: #12
```

### Development Setup

(To be completed as implementation begins)

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up environment variables from `.env.example`
5. Run tests to validate setup

### Testing Strategy

#### Unit Testing
- Test individual components in isolation
- Focus on EFL calculations, memory operations, response generation
- Use pytest with fixtures for consistent test data

#### Integration Testing
- Test interaction between EFL, memory, and response generation
- Validate emotional coherence across conversation sequences
- Test LLM provider abstractions

#### Research Validation
- Real-world prototype testing (as in April 2026 counseling trial)
- Evaluate trauma-informed interaction pattern success
- Measure tonal coherence and identity consistency metrics

## Key Development Principles

### 1. Research-First Mindset
- Every significant decision should reference relevant research
- Document the papers and concepts informing architectural choices
- Validate novel approaches with empirical testing before scaling

### 2. Emotional Coherence
- Maintain consistency in emotional tone across conversation
- Ensure responses honor the emotional context established by EFL
- Validate that identity persists through context transitions

### 3. Safety & Trauma-Informed Design
- Design with awareness of potential emotional harm
- Implement safeguards based on trauma-informed care principles
- Test thoroughly in appropriate contexts before deployment

### 4. Modular Architecture
- Keep EFL, memory, and response generation loosely coupled
- Enable independent testing and iteration
- Support integration with the broader CCCS Framework

### 5. Explicit Over Implicit
- Use clear, descriptive names for emotional states and patterns
- Document the assumptions embedded in constraint geometry encodings
- Make tonal parameters explicit and adjustable

## Integration with CCCS Framework

This project implements key components of the **CCCS 7-Layer Architecture**:

| Layer | Responsibility | Component |
|-------|---|---|
| Layer 5 | Emotional Feedback Loop | EFL implementation with real-time state tracking |
| Layer 6 | Tone Engine | Persona rendering and tonal coherence maintenance |
| Layer 7 | Self-Reference Engine | Identity consistency and relational memory |

### Related Projects
- **[Cognitive Pattern Tools](https://github.com/aadi-architect/cognitive-pattern-tools)** - Analyzes patterns extracted from EFL states
- **[Decision Simulation Framework](https://github.com/aadi-architect/decision-simulation-framework)** - Uses emotional states to simulate decision outcomes
- **[CCCS Framework](https://github.com/aadi-architect/aadi-architect)** - Parent research architecture

## Guidance for AI Assistants

### When Adding Features
1. **Understand the research context**: Read relevant sections of this document and README.md
2. **Maintain architectural principles**: Respect the three pillars and modular design
3. **Document decisions**: Explain WHY not just WHAT in commit messages
4. **Reference research**: Include academic citations where appropriate
5. **Test comprehensively**: Include unit tests, integration tests, and research validation tests

### When Fixing Bugs
- Identify whether the bug affects emotional coherence or identity consistency
- Ensure the fix doesn't violate trauma-informed design principles
- Add regression tests to prevent similar issues

### When Proposing Changes
- Consider impact on the EFL formula and emotional state tracking
- Evaluate implications for symbolic memory and tonal coherence
- Assess alignment with CCCS Framework integration

### Code Quality Standards
- Type hints for all functions (Python 3.10+)
- Docstrings for public APIs (one-line for simple functions, multi-line with examples for complex ones)
- 80-character line limit with exceptions for long strings and URLs
- Follow PEP 8 with project-specific conventions documented below

## Use Cases & Scope

This system is designed for:
- **AI Companions & Personal Assistants**: Long-term relational AI that remembers emotional context
- **Mental-Health Decision-Support Systems**: Emotionally aware guidance for mental health contexts
- **Adaptive Learning**: Emotional scaffolding that adjusts to learner's affective state
- **Voice-Based Counseling Prototypes**: Direct real-world application with trauma-informed patterns

Not designed for:
- General-purpose chatbots (unnecessary architectural complexity)
- Systems without emotional awareness requirements
- Fully autonomous decision-making in critical contexts

## Future Development Roadmap

### Phase 1: Core Implementation (Current)
- [ ] Implement EFL with formula and state management
- [ ] Build constraint geometry encoding for symbolic memory
- [ ] Develop adaptive response generation with persona engine
- [ ] Create LLM provider abstractions

### Phase 2: Voice Integration
- [ ] Full ElevenLabs voice integration
- [ ] Real-time EFL state updates from voice context
- [ ] Validate tonal coherence in speech output

### Phase 3: Production Scaling
- [ ] Performance optimization for low-latency emotional feedback
- [ ] Distributed memory architecture for large conversation histories
- [ ] Comprehensive evaluation metrics and monitoring

### Phase 4: Research Publication
- [ ] Document novel findings and validate approach
- [ ] Publish papers on emotional feedback mechanisms
- [ ] Open-source refined implementations

## Contact & Questions

**Project Lead:** Adarsh Kumar (Aadi)  
📧 **Email:** adarshkr26@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/adarshkumar-ai-research](https://linkedin.com/in/adarshkumar-ai-research)

For questions about:
- **Architecture & Design**: Reference CLAUDE.md and documentation/
- **Research Context**: See README.md and research papers cited in commits
- **Integration**: Consult integration_guide.md and related project repositories
- **Implementation Details**: Check code comments and docstrings

## Document History

- **2026-05-10**: Initial CLAUDE.md creation with comprehensive architecture documentation

---

**Last Updated:** 2026-05-10  
**Branch:** claude/add-claude-documentation-1yi5i  
**Status:** 🚧 Active Research & Documentation Phase
