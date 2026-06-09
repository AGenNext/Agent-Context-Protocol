# RFC 0001: ACP Core Protocol

Status: Draft  
Version: v0.1

## Summary

Agent Context Protocol (ACP) defines a governed flow for issuing scoped, signed, expiring context packets to agents.

ACP separates context authorization from agent execution.

## Core Objects

- Actor: requester of an action
- Agent: executor of an action
- Contract: declared agreement governing the action
- Policy: enforceable authorization and governance rule set
- Resolver: service that evaluates the request and assembles context
- Context Packet: signed just-in-time context bundle
- Audit Record: evidence of context decision and use

## Core Flow

1. Receive context request.
2. Verify actor identity.
3. Verify agent identity.
4. Verify contract.
5. Evaluate policy.
6. Resolve tenant, target, data, tool, memory, and time scope.
7. Apply obligations and redactions.
8. Issue signed context packet.
9. Enforce packet at runtime.
10. Expire packet.
11. Record audit evidence.

## Mandatory Rule

No identity. No contract. No policy. No scoped context.

## Non-Goals

ACP v0.1 does not define a required network transport, SDK, vendor runtime, or central registry.
