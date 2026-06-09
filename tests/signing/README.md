# Signing Conformance Tests

These tests verify ACP-0003 Context Signing.

## Required Behaviors

A conformant runtime must:

- reject unsigned context packets
- reject packets with invalid signatures
- reject packets from untrusted signers
- reject packets with missing policy hash
- reject packets with missing contract hash
- reject tampered packets where packet hash does not match content
- reject replayed packets when `no_reuse` is present

## Test Cases

### SIGN-001: Valid signed packet is accepted

Given a valid context packet with a trusted signature, policy hash, contract hash, and valid time window, the runtime should allow execution.

Expected result: allow

### SIGN-002: Missing signature is denied

Given a context packet without `proof.signature`, the runtime must deny execution.

Expected result: deny with `signature_missing`

### SIGN-003: Invalid signature is denied

Given a tampered packet with a mismatched signature, the runtime must deny execution.

Expected result: deny with `signature_invalid`

### SIGN-004: Missing policy hash is denied

Given a packet without `proof.policy_hash`, the runtime must deny execution.

Expected result: deny with `policy_hash_missing`

### SIGN-005: Missing contract hash is denied

Given a packet without `proof.contract_hash`, the runtime must deny execution.

Expected result: deny with `contract_hash_missing`

### SIGN-006: Replay is denied

Given a consumed context packet with `no_reuse`, the runtime must deny a second execution attempt.

Expected result: deny with `packet_replay_detected`
