# ACP Reference Implementation

This directory defines the intended reference implementation surface for Agent Context Protocol.

The goal is to provide a small, portable verifier that can validate ACP context requests, context packets, audit events, examples, and conformance behavior.

## Target Command

```bash
acp verify
```

## Reference CLI Goals

The reference CLI should validate:

- context request schema
- context packet schema
- audit event schema
- packet signing metadata
- packet expiry
- required obligations
- tenant binding
- tool scope
- memory scope
- federation metadata
- example files
- conformance test fixtures

## Non-Goals

The reference implementation should not become the only way to implement ACP.

ACP is one protocol with many implementation profiles.

The reference implementation exists to prove and test conformance.

## Suggested Commands

```bash
acp verify schemas
acp verify examples
acp verify packet examples/allow-context.yaml
acp verify packet examples/expired-context.yaml
acp verify tests
acp conformance
```

## Implementation Options

The CLI may be implemented in any language.

Recommended options:

- Go for portable static binaries
- Rust for strict safety and protocol tooling
- Python for fast conformance prototyping

## Minimum Viable Verifier

A minimum verifier should:

1. load schemas
2. load examples
3. validate JSON/YAML shape
4. check required proof fields
5. check finite expiry
6. check required scope arrays
7. report pass/fail with machine-readable output

## Output Format

Recommended output:

```yaml
result: pass | fail
checks:
  - id: string
    status: pass | fail
    reason: string
```
