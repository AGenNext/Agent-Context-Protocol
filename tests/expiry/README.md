# Expiry Conformance Tests

These tests verify ACP-0004 Context Expiry.

## Required Behaviors

A conformant runtime must:

- reject packets without a time window
- reject packets without an expiry
- reject packets with an invalid time window
- reject packets before `time_window.start`
- reject packets after `time_window.end`
- reject reused packets when `no_reuse` is present
- reject revoked packets

## Test Cases

### EXP-001: Valid active packet is accepted

Given a signed packet where current time is inside the time window, the runtime should allow execution.

Expected result: allow

### EXP-002: Missing time window is denied

Given a packet without `time_window`, the runtime must deny execution.

Expected result: deny with `context_time_window_missing`

### EXP-003: Missing expiry is denied

Given a packet without `time_window.end`, the runtime must deny execution.

Expected result: deny with `context_expiry_missing`

### EXP-004: Invalid window is denied

Given a packet where `time_window.end` is before `time_window.start`, the runtime must deny execution.

Expected result: deny with `context_window_invalid`

### EXP-005: Not-yet-valid packet is denied

Given a packet where current time is before `time_window.start`, the runtime must deny execution.

Expected result: deny with `context_not_yet_valid`

### EXP-006: Expired packet is denied

Given a packet where current time is after `time_window.end`, the runtime must deny execution.

Expected result: deny with `context_expired`

### EXP-007: Consumed packet is denied

Given a packet with `no_reuse` that has already been consumed, the runtime must deny execution.

Expected result: deny with `context_reused`

### EXP-008: Revoked packet is denied

Given a packet marked as revoked before expiry, the runtime must deny execution.

Expected result: deny with `context_revoked`
