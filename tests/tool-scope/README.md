# Tool Scope Conformance Tests

These tests verify ACP-0006 Tool Authorization.

## Required Behaviors

A conformant runtime must:

- reject tool use when the tool is not in `allowed_tools`
- reject tool use when the tool is in `denied_tools`
- reject tool use after context expiry
- reject tool use with unsigned context
- reject tool use across tenant boundary
- reject tool use when contract does not allow the tool
- reject tool use when requested tool action exceeds target scope

## Test Cases

### TOOL-001: Allowed tool is accepted

Given a signed active packet where the requested tool is listed in `allowed_tools`, the runtime should allow the tool call.

Expected result: allow

### TOOL-002: Missing tool scope is denied

Given a packet without the requested tool in `allowed_tools`, the runtime must deny the tool call.

Expected result: deny with `tool_not_allowed`

### TOOL-003: Explicitly denied tool is denied

Given a packet where the requested tool is listed in `denied_tools`, the runtime must deny the tool call.

Expected result: deny with `tool_explicitly_denied`

### TOOL-004: Expired context denies tool use

Given an expired packet, the runtime must deny the tool call even if the tool appears in `allowed_tools`.

Expected result: deny with `tool_context_expired`

### TOOL-005: Unsigned context denies tool use

Given an unsigned packet, the runtime must deny the tool call.

Expected result: deny with `tool_signature_invalid`

### TOOL-006: Cross-tenant tool is denied

Given a requested tool scoped to another tenant, the runtime must deny the tool call.

Expected result: deny with `tool_tenant_boundary_violation`

### TOOL-007: Tool action exceeds context scope

Given a packet that permits a read-only tool action, the runtime must deny a write or export operation.

Expected result: deny with `tool_policy_denied`
