# ACP-0006: Tool Authorization

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0006 defines how tools are authorized, scoped, denied, and audited in Agent Context Protocol runtimes.

Tools are not globally available to agents. A tool may be used only when the context packet explicitly allows that tool for the current actor, agent, tenant, contract, action, target, and time window.

## Core Rule

No tool use without scoped authorization.

## Tool Scope

A context packet must distinguish allowed and denied tools.

```yaml
allowed_tools: []
denied_tools: []
```

A runtime must deny tool execution if the tool is not present in `allowed_tools`.

## Required Tool Binding

Tool authorization must be bound to:

- actor
- agent
- tenant
- contract
- intent
- action
- target
- time window

## Tool Policy Inputs

A tool authorization decision should evaluate:

- tool identity
- tool capability
- tool risk level
- requested action
- target resource
- tenant boundary
- actor role
- agent trust level
- contract obligations
- data sensitivity
- audit requirement

## Denial Conditions

A runtime must deny tool use when:

- tool is not listed in `allowed_tools`
- tool is listed in `denied_tools`
- packet is expired
- packet is unsigned
- tenant boundary is violated
- contract does not allow tool use
- policy denies tool capability
- tool requires secrets not authorized by policy
- requested tool action exceeds context scope

## Tool Call Audit

Every privileged tool call should produce an audit event.

Recommended fields:

```yaml
context_id: string
agent: agent_id
tool: tool_id
action: action_id
target: resource_id
tenant: tenant_id
allowed: boolean
reason: string
timestamp: datetime
```

## Failure Modes

- tool_not_allowed
- tool_explicitly_denied
- tool_scope_missing
- tool_policy_denied
- tool_secret_denied
- tool_tenant_boundary_violation
- tool_context_expired
- tool_signature_invalid

## Conformance

A production ACP implementation must deny tool execution unless the signed context packet explicitly permits the tool for the current action and target.
