# ACP Implementation Profiles

Agent Context Protocol is one protocol.

ACP defines the required behavior for just-in-time, signed, scoped, auditable context packets.

ACP does not mandate one implementation architecture.

Different systems may implement ACP through different profiles, as long as they satisfy the same protocol invariants and conformance requirements.

## Core Rule

One protocol. Multiple implementation profiles.

## Protocol vs Profile

| Layer | Meaning |
|---|---|
| Protocol | The required behavior and invariants of ACP |
| Profile | A deployment or integration pattern used to implement ACP |
| Runtime | The concrete software that executes the profile |
| Conformance | Evidence that the runtime satisfies ACP |

The protocol must remain stable.

Profiles may vary by environment, language, platform, and deployment model.

## Valid Implementation Profiles

### Gateway Profile

ACP is enforced at an API gateway or agent gateway before requests reach agent runtimes, tools, memory, or data systems.

### Sidecar Profile

ACP is enforced by a sidecar process deployed next to an agent runtime or service workload.

### Library Profile

ACP is implemented as an application library embedded directly into an agent framework, service, or runtime.

### Runtime-Native Profile

ACP is implemented as a native capability of the agent runtime itself.

### Kubernetes Controller Profile

ACP is implemented through Kubernetes-native controllers, custom resources, admission controls, and reconciliation loops.

### Policy-Engine Profile

ACP is implemented using a policy engine such as OPA, Cedar, OpenFGA, AuthZEN-compatible authorization services, or equivalent systems.

### Database-Native Profile

ACP is implemented close to the data layer using database-native access control, row-level policy, graph permissions, functions, triggers, or audit records.

### Service-Mesh Profile

ACP is implemented through mesh-level identity, authorization, telemetry, and traffic policy.

### Agent-Framework Adapter Profile

ACP is implemented as an adapter for an agent framework, tool-calling framework, MCP server, A2A endpoint, or orchestration layer.

### Hybrid Profile

ACP is implemented through a combination of gateway, runtime, policy, database, mesh, controller, and adapter enforcement.

## Conformance Boundary

An implementation profile is ACP-conformant only if it enforces:

- identity binding
- agent binding
- tenant binding
- contract binding
- policy evaluation
- target scope
- tool scope
- memory scope
- context signing
- context expiry
- audit trail
- no cross-tenant context
- no reuse after expiry

The profile can vary. The protocol cannot.

## Non-Conformant Claims

A system is not ACP-conformant merely because it:

- stores context
- retrieves memory
- calls tools
- logs prompts
- uses a policy engine
- runs in Kubernetes
- has a gateway
- signs arbitrary payloads

ACP conformance requires the full protocol behavior defined by the ACP specification and conformance requirements.

## Recommended Production Pattern

Production deployments should prefer defense in depth:

```text
Gateway
  + Runtime enforcement
  + Policy engine
  + Data-layer controls
  + Audit trail
```

No single profile is mandatory.

The implementation must prove conformance at the boundary where context becomes executable.
