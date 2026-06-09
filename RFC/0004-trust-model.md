# RFC 0004: ACP Trust Model

Status: Draft
Version: v0.1

## Summary

ACP defines trust as verifiable evidence that context was requested, authorized, assembled, delivered, and used according to contract and policy.

Trust is derived from evidence, not assumptions.

## Trust Layers

### Identity Trust

Verifies actor and agent identities.

Evidence:
- DID
- credentials
- signatures
- organizational assertions

### Contract Trust

Verifies the existence and validity of a governing contract.

Evidence:
- contract identifier
- contract version
- contract hash

### Policy Trust

Verifies that authorization decisions were evaluated.

Evidence:
- policy id
- policy hash
- decision record

### Context Trust

Verifies that the packet delivered matches the approved scope.

Evidence:
- scope summary
- redaction evidence
- packet signature

### Execution Trust

Verifies that the agent executed within packet boundaries.

Evidence:
- execution logs
- tool invocations
- scope checks

### Audit Trust

Verifies that evidence exists after execution.

Evidence:
- audit records
- trace identifiers
- replay records

## Trust Score

Future ACP versions may define a portable trust score derived from identity, contract, policy, execution, and audit evidence.

ACP v0.1 does not standardize trust scoring.
