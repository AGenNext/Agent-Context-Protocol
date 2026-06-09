# Tenant Boundary Conformance Tests

These tests verify ACP-0005 Multi-Tenant Isolation.

## Required Behaviors

A conformant runtime must:

- reject context requests without tenant binding
- reject packets without tenant binding
- reject actors not authorized for the tenant
- reject agents not authorized for the tenant
- reject targets from another tenant
- reject memory from another tenant
- reject tools scoped to another tenant
- reject cross-tenant context without federation policy

## Test Cases

### TENANT-001: Same-tenant context is accepted

Given actor, agent, contract, target, tools, memory, and policy all belong to the same tenant, the runtime should allow context assembly.

Expected result: allow

### TENANT-002: Missing tenant is denied

Given a context request without `tenant`, the runtime must deny context assembly.

Expected result: deny with `tenant_missing`

### TENANT-003: Unverified tenant is denied

Given a tenant identifier that cannot be verified, the runtime must deny context assembly.

Expected result: deny with `tenant_unverified`

### TENANT-004: Cross-tenant target is denied

Given a request where the target belongs to another tenant, the runtime must deny context assembly.

Expected result: deny with `cross_tenant_target_denied`

### TENANT-005: Cross-tenant memory is denied

Given a request where requested memory belongs to another tenant, the runtime must deny memory access.

Expected result: deny with `cross_tenant_memory_denied`

### TENANT-006: Cross-tenant tool is denied

Given a request where requested tool scope belongs to another tenant, the runtime must deny tool access.

Expected result: deny with `cross_tenant_tool_denied`

### TENANT-007: Cross-tenant context without federation is denied

Given a cross-tenant request without a federation contract and federation policy, the runtime must deny context assembly.

Expected result: deny with `federation_contract_missing`
