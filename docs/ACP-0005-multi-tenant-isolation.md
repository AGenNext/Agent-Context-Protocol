# ACP-0005: Multi-Tenant Isolation

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0005 defines tenant isolation requirements for Agent Context Protocol implementations.

A context packet must be bound to one tenant and must not expose context, tools, memory, knowledge, contracts, policies, secrets, or audit data from another tenant unless an explicit federation policy allows it.

## Core Rule

No cross-tenant context.

## Tenant Binding

Every ACP request and context packet must include a tenant identifier.

```yaml
tenant: tenant_id
```

The tenant must be resolved before context assembly.

## Tenant-Scoped Resources

The following resources must be tenant-scoped:

- identity graph
- authorization graph
- contracts
- policies
- memory
- knowledge
- tools
- secrets
- data catalogs
- audit logs

## Mandatory Denial

The runtime must deny context assembly if:

- tenant cannot be verified
- actor is not authorized in tenant
- agent is not authorized in tenant
- target belongs to another tenant
- memory belongs to another tenant
- tool scope crosses tenant boundary
- contract does not apply to tenant
- policy does not apply to tenant

## Federation Exception

Cross-tenant context may be allowed only when all are true:

- federation contract exists
- source tenant permits sharing
- destination tenant permits receiving
- policy permits the specific action
- data scope is explicit
- redaction is applied
- audit is written in both tenant contexts

## Failure Modes

- tenant_missing
- tenant_unverified
- tenant_boundary_violation
- cross_tenant_target_denied
- cross_tenant_memory_denied
- cross_tenant_tool_denied
- federation_contract_missing
- federation_policy_denied

## Conformance

A production ACP implementation must enforce tenant boundaries before context assembly and before tool, data, memory, or knowledge access.
