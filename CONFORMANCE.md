# ACP Conformance

An implementation is ACP-conformant only if it satisfies every mandatory invariant.

ACP conformance is based on observable behavior, not implementation language, framework, or vendor choice.

## Required Checks

| Check | Required |
|---|---|
| Actor identity verified | Yes |
| Agent identity verified | Yes |
| Tenant boundary enforced | Yes |
| Contract verified | Yes |
| Policy evaluated | Yes |
| Target scope resolved | Yes |
| Data scope resolved | Yes |
| Tool scope resolved | Yes |
| Memory permission checked | Yes |
| Unauthorized data redacted | Yes |
| Context packet signed | Yes |
| Context packet expires | Yes |
| Context use audited | Yes |
| Reuse after expiry denied | Yes |

## Mandatory Invariants

- no context without identity
- no context without agent
- no context without tenant
- no context without contract
- no context without policy
- no context without target scope
- no tool context without scope
- no memory context without permission
- no secret context without policy
- no cross-tenant context
- no context reuse after expiry
- no unsigned context packet
- no execution without audit trail

## Non-Conformant Behavior

The following are ACP violations:

- passing full memory into an agent without scope
- allowing tools without policy resolution
- reusing context from a prior action
- sharing context across tenants
- executing with unsigned context
- failing to audit context use
- exporting context without obligation checks
- allowing context after expiry
- skipping redaction when policy denies fields

## Conformance Levels

### ACP-L0: Documented

The implementation documents ACP concepts but does not enforce them.

This level is not production conformant.

### ACP-L1: Enforced Context Request

The implementation validates actor, agent, intent, contract, action, target, tenant, and time window before assembling context.

### ACP-L2: Scoped Context Packet

The implementation produces a scoped context packet with allowed and denied actions, tools, data, memory, obligations, and expiry.

### ACP-L3: Signed Runtime Context

The implementation signs the context packet and denies execution if the signature is invalid or expired.

### ACP-L4: Audited Multi-Tenant Runtime

The implementation enforces tenant isolation, writes audit records for context use, and prevents reuse after expiry.

### ACP-L5: Verifiable Protocol Runtime

The implementation provides machine-readable proofs, policy hashes, contract hashes, and repeatable conformance tests.

## Minimum Production Conformance

Production systems must satisfy ACP-L4 or higher.

## Test Evidence

A conformant implementation should provide evidence for:

- accepted context request
- denied context request
- redacted context packet
- expired context packet
- cross-tenant denial
- tool-scope denial
- memory-scope denial
- audit record creation
