# ACP-0010: Context Federation

Status: Draft
Version: 0.1.0
Protocol: Agent Context Protocol

## Abstract

ACP-0010 defines how context may cross organizational, tenant, platform, or trust boundaries while preserving ACP guarantees.

Federation is the exception, not the default.

## Core Rule

No cross-boundary context without federation policy.

## Federation Requirements

Context federation requires:

- source identity verification
- destination identity verification
- source tenant authorization
- destination tenant authorization
- federation contract
- federation policy
- scoped data sharing
- scoped memory sharing
- auditability
- provenance preservation
- signed context packets

## Federation Contract

A federation contract defines:

- participating parties
- permitted actions
- permitted data classes
- permitted memory classes
- obligations
- retention rules
- revocation rules
- audit requirements

Federation must be denied when a federation contract is missing.

## Federation Packet Rules

Federated packets must:

- remain signed
- preserve provenance
- preserve redactions
- preserve obligations
- preserve expiry
- preserve tenant identity
- preserve contract references

A receiving system must not silently expand scope.

## Scope Reduction

Federation may reduce scope.

Federation must not increase scope beyond what the source packet permits.

Allowed:

```text
full scope -> reduced scope
```

Denied:

```text
reduced scope -> expanded scope
```

## Cross-Boundary Audit

Federated actions should generate audit evidence in both participating environments.

Recommended fields:

```yaml
federation_id: string
source_tenant: tenant_id
destination_tenant: tenant_id
context_id: string
contract: contract_id
action: action_id
timestamp: datetime
```

## Revocation

A federation participant may revoke access according to federation contract terms.

Revocation should invalidate future packet issuance and future context exchanges.

## Failure Modes

- federation_contract_missing
- federation_policy_denied
- federation_identity_unverified
- federation_tenant_denied
- federation_scope_expansion_detected
- federation_provenance_missing
- federation_signature_invalid
- federation_audit_missing

## Conformance

A production ACP implementation must deny cross-boundary context exchange unless federation identity, policy, contract, provenance, signing, expiry, and audit requirements are satisfied.
