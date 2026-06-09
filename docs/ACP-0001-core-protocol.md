# ACP-0001: Core Protocol

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0001 defines the core Agent Context Protocol.

The protocol governs how an agent requests, receives, uses, expires, and audits context for a specific action.

ACP treats context as a just-in-time runtime authority packet, not as static memory.

## Core Principle

No identity. No contract. No policy. No scoped context.

## Problem

Agent systems commonly pass broad, stale, or unauthorized context into models and tools. This creates privacy, compliance, safety, tenant isolation, and audit failures.

ACP prevents this by requiring every context packet to be resolved from a specific actor, agent, intent, contract, action, target, tenant, and time window.

## Protocol Actors

- Actor: the human, service, organization, or agent requesting action
- Agent: the runtime unit that will execute the action
- Context Authority: the component that resolves, signs, expires, and audits context
- Policy Engine: the component that evaluates rules
- Contract Store: the component that binds allowed obligations and responsibilities
- Audit Store: the component that records context use

## Required Request Fields

A conformant ACP request must include:

- actor
- agent
- intent
- contract
- action
- target
- tenant
- time_window

## Resolution Flow

1. Verify actor identity
2. Verify agent identity
3. Verify tenant boundary
4. Verify contract
5. Evaluate policy
6. Resolve permissions
7. Resolve target scope
8. Resolve data scope
9. Resolve memory scope
10. Resolve tool scope
11. Apply redactions
12. Assemble context
13. Attach obligations
14. Sign context packet
15. Execute with context
16. Expire context
17. Audit context use

## Mandatory Denials

A conformant implementation must deny context assembly when:

- actor identity cannot be verified
- agent identity cannot be verified
- tenant boundary cannot be enforced
- contract is missing
- policy denies the action
- target scope is missing
- tool scope is missing for tool use
- memory permission is missing for memory use
- the packet is unsigned
- the packet is expired

## Output

The protocol produces a signed just-in-time context packet.

```yaml
type: signed_jit_context_packet
```

## Conformance

Production systems must satisfy ACP-L4 or higher as defined in `CONFORMANCE.md`.
