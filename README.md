# Agent Context Protocol

Agent Context Protocol (ACP) defines how context is assembled, authorized, signed, used, expired, and audited for agent actions.

ACP treats context as a governed runtime packet, not a static memory dump.

An agent does not receive context directly. It requests context for a specific actor, intent, contract, action, target, and time window. The protocol resolves identity, policy, permissions, tool scope, data scope, obligations, redactions, and audit requirements before producing a signed just-in-time context packet.

## Core Rule

No identity. No contract. No policy. No scoped context.

## Why ACP Exists

Modern agents often fail because context is:

- too broad
- stale
- unscoped
- reused
- unauthorized
- disconnected from contracts
- disconnected from audit

ACP prevents this by making context temporary, signed, scoped, explainable, and auditable.

## Protocol Flow

1. Verify actor
2. Verify agent
3. Verify contract
4. Check policy
5. Resolve permissions
6. Resolve target scope
7. Resolve tool scope
8. Assemble context
9. Redact unauthorized data
10. Sign context packet
11. Execute action with context
12. Expire packet
13. Audit context use

## Output

ACP produces a signed just-in-time context packet.

```yaml
type: signed_jit_context_packet
```

## Invariants

- no context without identity
- no context without contract
- no context without policy
- no tool context without scope
- no memory context without permission
- no cross-tenant context
- no context reuse after expiry
