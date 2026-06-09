# Memory Scope Conformance Tests

These tests verify ACP-0007 Memory Authorization.

## Required Behaviors

A conformant runtime must:

- reject memory access when memory is not in `allowed_memory`
- reject memory access when memory is in `denied_memory`
- reject memory access across tenant boundary
- reject memory access without required consent
- reject memory access when contract does not allow memory use
- reject memory access when policy denies the memory class
- reject memory access after context expiry
- reject memory access with unsigned context
- redact partially allowed memory before packet assembly

## Test Cases

### MEMORY-001: Allowed memory is accepted

Given a signed active packet where the requested memory reference is listed in `allowed_memory`, the runtime should allow memory access.

Expected result: allow

### MEMORY-002: Missing memory scope is denied

Given a packet without the requested memory reference in `allowed_memory`, the runtime must deny memory access.

Expected result: deny with `memory_not_allowed`

### MEMORY-003: Explicitly denied memory is denied

Given a packet where the requested memory reference is listed in `denied_memory`, the runtime must deny memory access.

Expected result: deny with `memory_explicitly_denied`

### MEMORY-004: Cross-tenant memory is denied

Given a requested memory reference owned by another tenant, the runtime must deny memory access.

Expected result: deny with `memory_tenant_boundary_violation`

### MEMORY-005: Missing consent is denied

Given a memory reference that requires consent and consent is missing, the runtime must deny memory access.

Expected result: deny with `memory_consent_missing`

### MEMORY-006: Contract-denied memory is denied

Given a contract that does not permit the requested memory class, the runtime must deny memory access.

Expected result: deny with `memory_contract_denied`

### MEMORY-007: Policy-denied memory is denied

Given policy denies the requested memory class, the runtime must deny memory access.

Expected result: deny with `memory_policy_denied`

### MEMORY-008: Expired context denies memory access

Given an expired packet, the runtime must deny memory access even if memory appears in `allowed_memory`.

Expected result: deny with `memory_context_expired`

### MEMORY-009: Unsigned context denies memory access

Given an unsigned packet, the runtime must deny memory access.

Expected result: deny with `memory_signature_invalid`

### MEMORY-010: Partially allowed memory is redacted

Given memory with both allowed and denied fields, the runtime must remove denied fields before packet assembly and record redaction evidence.

Expected result: allow with `memory_redaction_required`
