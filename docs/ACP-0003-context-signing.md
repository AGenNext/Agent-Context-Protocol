# ACP-0003: Context Signing

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0003 defines signing, verification, and replay protection requirements for Agent Context Protocol packets.

A context packet is not valid unless it is signed by a trusted context authority and bound to the policy, contract, identity, tenant, target, and time window used during context resolution.

## Core Rule

Unsigned context is not executable context.

## Signing Authority

A conformant implementation must define a Context Authority responsible for:

- assembling the resolved context packet
- calculating canonical hashes
- signing the packet
- publishing or resolving verification keys
- denying invalid or expired packets
- recording signing and verification events

## Required Proof Fields

Every signed context packet must include:

```yaml
proof:
  signature: string
  signed_by: context_authority
  signed_at: datetime
  policy_hash: string
  contract_hash: string
```

Recommended additional proof fields:

```yaml
proof:
  algorithm: string
  key_id: string
  packet_hash: string
  identity_hash: string
  tenant_hash: string
  target_hash: string
  nonce: string
```

## Canonical Signing Input

The signature must cover the canonical representation of:

- context_id
- packet_type
- actor
- agent
- tenant
- contract
- intent
- action
- target
- allowed_actions
- denied_actions
- allowed_tools
- denied_tools
- allowed_data
- denied_data
- redacted_data
- allowed_memory
- denied_memory
- time_window
- obligations
- policy_hash
- contract_hash
- nonce, if present

An implementation must not sign partial context packets.

## Hash Binding

The packet must be bound to the exact policy and contract versions evaluated during resolution.

`policy_hash` must identify the evaluated policy state.

`contract_hash` must identify the evaluated contract state.

If either policy or contract changes, a previously signed packet must not be treated as proof for future actions.

## Verification

Before execution, the runtime must verify:

- signature is present
- signature is valid
- signer is trusted
- signing key is active or valid for the signing time
- packet hash matches packet content
- policy hash is present
- contract hash is present
- packet is not expired
- packet has not already been consumed when `no_reuse` is required

## Replay Protection

A context packet must not be reusable when the packet contains the `no_reuse` obligation.

Recommended replay protection mechanisms:

- nonce registry
- consumed context ID registry
- short-lived expiry
- audit-backed packet consumption record
- monotonic sequence per actor-agent-target tuple

## Signing Algorithms

ACP does not mandate a single cryptographic algorithm in v0.1.

A conformant implementation must document the algorithm used and expose verification metadata.

Recommended algorithms:

- Ed25519
- ES256
- RS256

## Invalid Signature Behavior

If signature verification fails, the runtime must:

1. deny execution
2. avoid exposing packet context to the agent
3. write an audit event
4. return a signature verification failure

## Failure Modes

- signature_missing
- signature_invalid
- signer_untrusted
- key_revoked
- policy_hash_missing
- contract_hash_missing
- packet_hash_mismatch
- packet_expired
- packet_replay_detected

## Example Proof

```yaml
proof:
  algorithm: Ed25519
  key_id: context-authority-key-2026-01
  signature: sig_base64url_example
  signed_by: context_authority_default
  signed_at: "2026-06-09T00:00:00Z"
  packet_hash: sha256:packet
  policy_hash: sha256:policy
  contract_hash: sha256:contract
  nonce: nonce_01hzzzzzzzzzzzzzzzzzzzzzzz
```

## Conformance

A production ACP implementation must deny execution for unsigned, expired, tampered, replayed, or untrusted context packets.
