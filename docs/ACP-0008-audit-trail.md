# ACP-0008: Audit Trail

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0008 defines audit trail requirements for Agent Context Protocol implementations.

Every context request, context decision, packet issuance, tool use, memory use, denial, expiry, revocation, and execution event must be auditable.

## Core Rule

No execution without audit trail.

## Audit Scope

A conformant ACP implementation should produce audit records for:

- context request received
- actor verification
- agent verification
- tenant verification
- contract verification
- policy decision
- target scope resolution
- data scope resolution
- tool scope resolution
- memory scope resolution
- redaction applied
- context packet signed
- context packet verified
- context packet consumed
- tool call allowed or denied
- memory access allowed or denied
- context expired
- context revoked
- execution completed, failed, cancelled, or denied

## Required Audit Fields

Recommended minimum audit event fields:

```yaml
audit_id: string
context_id: string
event_type: string
actor: identity
agent: agent_id
tenant: tenant_id
contract: contract_id
action: action_id
target: resource_id
decision: allow | deny | redact | expire | revoke | audit
reason: string
timestamp: datetime
```

## Decision Evidence

Audit events should include enough evidence to explain the decision without exposing unauthorized context.

Recommended evidence fields:

```yaml
evidence:
  policy_hash: string
  contract_hash: string
  packet_hash: string
  rule_ids: []
  obligations: []
  redactions: []
```

## Audit Integrity

Audit records should be append-only.

Implementations should protect audit records against deletion, tampering, and unauthorized modification.

Recommended protections:

- append-only storage
- hash chaining
- signed audit events
- immutable object storage
- write-once retention policies
- tenant-scoped audit access

## Audit Privacy

Audit trails must not leak denied or redacted context.

Audit records should reference sensitive data by stable identifiers, hashes, or redaction markers rather than copying full sensitive payloads.

## Failure Behavior

If an audit record cannot be written for a required event, the runtime must choose a documented fail mode.

For high-risk or regulated actions, the runtime must fail closed.

## Failure Modes

- audit_write_failed
- audit_store_unavailable
- audit_integrity_failed
- audit_tenant_scope_violation
- audit_sensitive_data_leak_detected

## Conformance

A production ACP implementation must create audit evidence for context issuance, verification, use, denial, expiry, revocation, tool use, and memory use.
