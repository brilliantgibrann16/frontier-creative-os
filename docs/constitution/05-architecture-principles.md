# Article 5 — Architecture Principles

1. The platform maintains explicit boundaries between the language, compiler, runtime, AI, and SDK layers.
2. Architectural change is proposed through an RFC and recorded in an Architecture Decision Record before implementation.
3. Every component has a documented responsibility. Undocumented coupling between components is treated as a defect.
4. Interfaces between layers are specified before other layers depend on them.
5. Performance claims require measurement. No optimization is accepted on assertion alone.
