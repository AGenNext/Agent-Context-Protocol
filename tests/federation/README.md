# Federation Conformance Tests

These tests verify ACP-0010 Context Federation.

## Required Behaviors

A conformant runtime must:

- reject cross-boundary context without a federation contract
- reject cross-boundary context without federation policy
- reject unverified source identity
- reject unverified destination identity
- reject unauthorized source tenant sharing
- reject unauthorized destination tenant receiving
- reject scope expansion during federation
- preserve expiry during federation
- preserve redactions during federation
- preserve provenance during federation
- preserve auditability across boundaries
- reject invalid federated signatures

## Test Cases

### FED-001: Valid federated context is accepted

Given a signed federated context packet with source tenant, destination tenant, federation contract, federation policy, provenance, redactions, and valid expiry, the runtime should allow the federated action.

Expected result: allow

### FED-002: Missing federation contract is denied

Given a cross-boundary context request without a federation contract, the runtime must deny federation.

Expected result: deny with `federation_contract_missing`

### FED-003: Federation policy denial is enforced

Given a federation policy that denies the requested action, the runtime must deny federation.

Expected result: deny with `federation_policy_denied`

### FED-004: Unverified source identity is denied

Given an unverified source identity, the runtime must deny federation.

Expected result: deny with `federation_identity_unverified`

### FED-005: Tenant authorization failure is denied

Given a source or destination tenant that does not authorize the exchange, the runtime must deny federation.

Expected result: deny with `federation_tenant_denied`

### FED-006: Scope expansion is denied

Given a federated packet that attempts to add actions, tools, data, or memory beyond the source packet scope, the runtime must deny federation.

Expected result: deny with `federation_scope_expansion_detected`

### FED-007: Missing provenance is denied

Given a federated packet without provenance evidence, the runtime must deny federation.

Expected result: deny with `federation_provenance_missing`

### FED-008: Invalid federated signature is denied

Given a federated packet with an invalid signature, the runtime must deny federation.

Expected result: deny with `federation_signature_invalid`

### FED-009: Missing federation audit is denied or fails closed

Given a high-risk federated action where audit cannot be written, the runtime must deny or fail closed according to policy.

Expected result: deny with `federation_audit_missing`
