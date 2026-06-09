# ACP-0002: Context Packet

Status: Draft  
Version: 0.1.0  
Protocol: Agent Context Protocol

## Abstract

ACP-0002 defines the canonical context packet format produced by the Agent Context Protocol.

A context packet is a signed, scoped, temporary runtime object that grants an agent access to only the context required for one action.

## Packet Type

```yaml
packet_type: signed_jit_context_packet
```

## Required Fields

A conformant ACP context packet must include:

```yaml
context_id: string
packet_type: signed_jit_context_packet
actor: identity
agent: agent_id
tenant: tenant_id
contract: contract_id
intent: intent_id
action: action_id
target: resource_id
allowed_actions: []
denied_actions: []
allowed_tools: []
denied_tools: []
allowed_data: []
denied_data: []
redacted_data: []
allowed_memory: []
denied_memory: []
time_window:
  start: datetime
  end: datetime
obligations: []
proof:
  signature: string
  signed_by: context_authority
  signed_at: datetime
  policy_hash: string
  contract_hash: string
```

## Identity Binding

The packet must bind context to:

- actor
- agent
- tenant
- contract
- intent
- action
- target

A packet that is not bound to all of these fields is not ACP-conformant.

## Scope Sections

### Action Scope

`allowed_actions` lists actions the agent may perform.

`denied_actions` lists actions explicitly denied by policy or contract.

### Tool Scope

`allowed_tools` lists tools available to the agent for this context packet.

`denied_tools` lists tools that were requested or discoverable but denied.

### Data Scope

`allowed_data` lists data references available to the agent.

`denied_data` lists data references unavailable to the agent.

`redacted_data` lists fields or records removed before packet assembly.

### Memory Scope

`allowed_memory` lists memory references allowed for the action.

`denied_memory` lists memory references denied by policy, tenant boundary, consent, or contract.

## Time Window

The packet must include a finite time window.

A packet without an expiry is invalid.

The context authority must deny use after `time_window.end`.

## Obligations

A conformant packet must include runtime obligations.

Recommended mandatory obligations:

- audit_required
- no_reuse
- no_export_without_policy
- expire_after_action
- preserve_provenance
- explain_context_sources

## Proof

The `proof` section binds the packet to the policy and contract state used during resolution.

The packet must include:

- signature
- signing authority
- signing time
- policy hash
- contract hash

## Invalid Packets

A packet is invalid if:

- it has no signature
- it has no expiry
- it lacks actor binding
- it lacks agent binding
- it lacks tenant binding
- it lacks contract binding
- it allows tools without tool scope
- it exposes memory without memory permission
- it contains unredacted denied data
- it is reused after expiry

## Example

```yaml
context_id: ctx_01hzzzzzzzzzzzzzzzzzzzzzzz
packet_type: signed_jit_context_packet
actor: user_123
agent: agent_research_001
tenant: tenant_acme
contract: contract_support_ops
action: summarize_ticket
target: ticket_456
intent: intent_customer_support
allowed_actions:
  - summarize_ticket
denied_actions:
  - export_customer_data
allowed_tools:
  - ticket_reader
denied_tools:
  - billing_admin
allowed_data:
  - ticket_456.subject
  - ticket_456.body
redacted_data:
  - ticket_456.payment_method
allowed_memory:
  - memory/customer_preferences/scoped_summary
denied_memory:
  - memory/full_customer_history
time_window:
  start: "2026-06-09T00:00:00Z"
  end: "2026-06-09T00:05:00Z"
obligations:
  - audit_required
  - no_reuse
  - expire_after_action
proof:
  signature: sig_example
  signed_by: context_authority_default
  signed_at: "2026-06-09T00:00:00Z"
  policy_hash: sha256:policy
  contract_hash: sha256:contract
```
