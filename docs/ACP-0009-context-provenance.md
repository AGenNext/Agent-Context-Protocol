# ACP-0009: Context Provenance

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0009 defines provenance requirements for Agent Context Protocol packets.

A context packet must preserve enough source, policy, contract, redaction, and transformation evidence to explain where context came from, why it was included, what was excluded, and how it changed before execution.

## Core Rule

No context without provenance.

## Provenance Scope

ACP provenance should cover:

- context request source
- identity source
- authorization source
- contract source
- policy source
- data source
- memory source
- knowledge source
- tool registry source
- redaction source
- transformation source
- signing source
- audit source

## Required Provenance Fields

Recommended minimum provenance fields:

```yaml
provenance:
  sources: []
  source_hashes: []
  policy_hash: string
  contract_hash: string
  packet_hash: string
  transformations: []
  redactions: []
  generated_at: datetime
  generated_by: context_authority
```

## Source References

Source references should be stable identifiers rather than copied sensitive payloads.

Recommended source reference fields:

```yaml
source:
  source_id: string
  source_type: identity | policy | contract | data | memory | knowledge | tool | audit
  tenant: tenant_id
  version: string
  hash: string
  accessed_at: datetime
```

## Transformations

If source context is summarized, filtered, embedded, normalized, translated, ranked, compressed, or otherwise transformed, the transformation should be recorded.

Recommended fields:

```yaml
transformation:
  transformation_id: string
  type: summarize | filter | redact | normalize | rank | embed | translate | compress
  input_refs: []
  output_ref: string
  performed_by: string
  performed_at: datetime
```

## Redaction Provenance

Redactions must be explainable without revealing the denied data.

Recommended fields:

```yaml
redaction:
  redaction_id: string
  source_ref: string
  field_ref: string
  reason: policy_denied | contract_denied | consent_missing | tenant_boundary | sensitivity
  rule_id: string
```

## Provenance Integrity

A context packet should bind provenance evidence into the packet proof through `packet_hash`, `policy_hash`, and `contract_hash`.

Implementations may also sign provenance records separately.

## Invalid Provenance Behavior

A runtime must not claim ACP provenance when:

- source references are missing
- policy hash is missing
- contract hash is missing
- transformations are hidden
- redactions are not recorded
- provenance crosses tenant boundary without federation policy
- provenance leaks denied data

## Failure Modes

- provenance_missing
- provenance_source_missing
- provenance_hash_missing
- provenance_redaction_missing
- provenance_transformation_missing
- provenance_tenant_boundary_violation
- provenance_sensitive_data_leak_detected

## Conformance

A production ACP implementation must preserve provenance evidence for context source selection, policy evaluation, contract binding, redaction, transformation, signing, and audit.
