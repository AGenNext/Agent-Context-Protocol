# ACP SDKs

Agent Context Protocol is one protocol.

SDKs are language-specific helpers for building, validating, signing, verifying, and consuming ACP artifacts.

SDKs must not redefine the protocol.

## Core Rule

One protocol. Many SDKs. Same conformance model.

## SDK Responsibilities

An ACP SDK should provide helpers for:

- context request construction
- context packet construction
- schema validation
- proof validation
- expiry checks
- tenant binding checks
- tool scope checks
- memory scope checks
- audit event construction
- provenance construction
- federation metadata validation

## SDK Non-Goals

An SDK must not:

- bypass ACP conformance
- create hidden context scope
- allow unsigned executable packets
- allow packets without expiry
- silently expand tenant, tool, data, or memory scope
- replace policy evaluation without recording evidence

## Initial SDK Targets

Recommended order:

1. Python SDK: fastest verifier and test harness
2. Go SDK: portable production verifier and gateway integration
3. Rust SDK: strict packet model and signing safety
4. TypeScript SDK: web, agent builder, and UI integration
5. Java SDK: enterprise platform integration

## Common SDK Surface

All SDKs should expose equivalent concepts:

```text
ContextRequest
ContextPacket
AuditEvent
Proof
TimeWindow
Obligation
Scope
Provenance
Federation
Verifier
```

## Required SDK Methods

Every SDK should eventually provide:

```text
validateRequest(request)
validatePacket(packet)
verifyProof(packet)
checkExpiry(packet, now)
checkToolScope(packet, tool)
checkMemoryScope(packet, memory)
buildAuditEvent(event)
verifyFederation(packet)
```

## Compatibility

SDKs must remain compatible with:

- schemas/context-request.schema.json
- schemas/context-packet.schema.json
- schemas/audit-event.schema.json
- CONFORMANCE.md
- docs/ACP-0001 through docs/ACP-0010

## Certification

An SDK should not claim ACP compatibility unless it passes the ACP conformance test suite.
