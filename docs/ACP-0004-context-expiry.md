# ACP-0004: Context Expiry

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0004 defines expiry, revocation, and consumption rules for Agent Context Protocol packets.

ACP context is just-in-time. A context packet must be temporary, bounded, and denied after its valid window or after one-time consumption when required by obligation.

## Core Rule

Context that does not expire is not ACP context.

## Required Time Window

Every ACP context packet must include:

```yaml
time_window:
  start: datetime
  end: datetime
```

The `end` value must be finite.

Packets without an expiry must be rejected.

## Expiry Semantics

A context packet is valid only when:

```text
now >= time_window.start
and
now <= time_window.end
```

After `time_window.end`, the packet is expired and must not be used for execution, tool calls, memory reads, data reads, or delegated actions.

## Expire After Action

When the packet includes this obligation:

```yaml
obligations:
  - expire_after_action
```

The packet must expire immediately after the authorized action completes, fails, or is cancelled.

## No Reuse

When the packet includes this obligation:

```yaml
obligations:
  - no_reuse
```

The runtime must reject any second use of the same `context_id`, even if the time window has not ended.

## Consumption Record

A conformant runtime should write a consumption record when a packet is used.

Recommended fields:

```yaml
context_id: string
consumed_by: agent_id
consumed_for: action_id
consumed_at: datetime
result: completed | failed | cancelled | denied
```

## Revocation

A context packet may be revoked before expiry.

Revocation must be supported when:

- actor access is revoked
- agent access is revoked
- tenant policy changes
- contract is suspended
- target is deleted or locked
- tool permission is removed
- memory permission is removed
- context compromise is suspected

## Revocation Check

Before execution and before each privileged tool, data, or memory access, the runtime should check whether the packet has been revoked.

For high-risk actions, revocation checking must be performed immediately before execution.

## Clock Handling

Implementations must document clock source and acceptable skew.

Recommended maximum skew:

```text
60 seconds
```

If skew cannot be resolved safely, the runtime must deny execution.

## Invalid Expiry Behavior

A runtime must deny execution when:

- the packet has no `time_window`
- `time_window.end` is missing
- `time_window.end` is before `time_window.start`
- current time is before `time_window.start`
- current time is after `time_window.end`
- packet has already been consumed under `no_reuse`
- packet is revoked

## Failure Modes

- context_time_window_missing
- context_expiry_missing
- context_window_invalid
- context_not_yet_valid
- context_expired
- context_reused
- context_revoked
- context_clock_skew_untrusted

## Example Expired Packet Denial

```yaml
error: context_expired
context_id: ctx_01hzzzzzzzzzzzzzzzzzzzzzzz
now: "2026-06-09T00:06:00Z"
time_window:
  start: "2026-06-09T00:00:00Z"
  end: "2026-06-09T00:05:00Z"
action: denied
```

## Conformance

A production ACP implementation must reject context packets that are expired, reused, revoked, not yet valid, or missing a finite expiry.
