# ACP Verifier Specification

Status: Draft  
Version: 0.1.0

## Purpose

The ACP verifier validates that ACP artifacts and packets satisfy the protocol, schema, and conformance requirements.

The target command is:

```bash
acp verify
```

## Minimum Effective Verifier

The minimum effective verifier must check:

1. schemas are valid JSON Schema
2. examples are valid YAML
3. examples match ACP packet requirements
4. context packet has `proof.signature`
5. context packet has `proof.policy_hash`
6. context packet has `proof.contract_hash`
7. context packet has finite expiry
8. denied examples are recognized as denied
9. expired examples are recognized as expired
10. federated examples have federation contract and policy

## Commands

```bash
acp verify schemas
acp verify examples
acp verify packet <path>
acp verify audit <path>
acp verify tests
acp conformance
```

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | All checks passed |
| 1 | Validation failed |
| 2 | Invalid input path |
| 3 | Schema load failure |
| 4 | Internal verifier error |

## Output

The verifier should support human-readable and machine-readable output.

Recommended machine-readable output:

```yaml
result: pass
checks:
  - id: ACP-PACKET-001
    status: pass
    reason: packet_type is signed_jit_context_packet
```

## Required Checks

### Packet Checks

- packet_type is `signed_jit_context_packet`
- context_id is present
- actor is present
- agent is present
- tenant is present
- contract is present
- intent is present
- action is present
- target is present
- time_window.start is present
- time_window.end is present
- proof.signature is present
- proof.policy_hash is present
- proof.contract_hash is present

### Expiry Checks

- time_window.end must be after time_window.start
- packet must not be valid outside the time window
- expired packets must be denied

### Scope Checks

- allowed and denied action arrays must exist
- allowed and denied tool arrays must exist
- allowed and denied memory arrays must exist
- redacted_data must exist

### Federation Checks

Federated examples must include:

- federation_id
- source_tenant
- destination_tenant
- federation_contract
- federation_policy
- provenance
- proof

## Non-Goals

The verifier does not need to execute agent workloads.

The verifier does not need to call real tools.

The verifier does not replace runtime authorization.

It proves whether artifacts and packets satisfy ACP structure and minimum conformance evidence.
