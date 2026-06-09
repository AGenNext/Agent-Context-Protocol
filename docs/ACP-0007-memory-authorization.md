# ACP-0007: Memory Authorization

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0007 defines how agent memory is authorized, scoped, redacted, denied, and audited.

Memory is not automatically available to an agent. Memory may be included in a context packet only when identity, tenant, contract, policy, target, purpose, and time-window checks allow it.

## Core Rule

No memory context without permission.

## Memory Scope

A context packet must distinguish allowed and denied memory.

```yaml
allowed_memory: []
denied_memory: []
```

A runtime must deny memory access if the memory reference is not present in `allowed_memory`.

## Memory Binding

Memory authorization must be bound to:

- actor
- agent
- tenant
- contract
- intent
- action
- target
- time window
- consent, where required

## Memory Classes

ACP implementations may classify memory by risk and scope.

Recommended classes:

- session_memory
- user_memory
- tenant_memory
- project_memory
- contract_memory
- tool_memory
- audit_memory
- public_knowledge_memory
- sensitive_memory
- regulated_memory

## Required Checks

Before memory is added to a context packet, the Context Authority must check:

- actor access
- agent access
- tenant boundary
- contract permission
- policy permission
- purpose limitation
- target relevance
- sensitivity level
- consent requirement
- retention rule
- redaction requirement

## Redaction

If memory is partially allowed, the Context Authority must redact denied fields before packet assembly.

Denied memory must not be hidden in prompts, tool metadata, embeddings, summaries, traces, or intermediate state.

## Denial Conditions

A runtime must deny memory access when:

- memory is not listed in `allowed_memory`
- memory is listed in `denied_memory`
- tenant boundary is violated
- consent is missing
- policy denies the memory class
- contract does not allow use
- action exceeds memory purpose
- packet is expired
- packet is unsigned
- packet has already been consumed under `no_reuse`

## Memory Audit

Every sensitive memory access should produce an audit event.

Recommended fields:

```yaml
context_id: string
actor: identity
agent: agent_id
tenant: tenant_id
memory_ref: string
action: action_id
target: resource_id
allowed: boolean
redacted: boolean
reason: string
timestamp: datetime
```

## Failure Modes

- memory_not_allowed
- memory_explicitly_denied
- memory_scope_missing
- memory_policy_denied
- memory_contract_denied
- memory_consent_missing
- memory_tenant_boundary_violation
- memory_redaction_required
- memory_context_expired
- memory_signature_invalid

## Conformance

A production ACP implementation must deny memory access unless the signed context packet explicitly permits the memory reference for the current action, target, tenant, and time window.
