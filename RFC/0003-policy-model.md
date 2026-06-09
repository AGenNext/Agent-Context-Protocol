# RFC 0003: ACP Policy Model

Status: Draft  
Version: v0.1

## Summary

ACP requires policy evaluation before context assembly and delivery.

Policy is not optional metadata. Policy is part of the context authorization path.

## Policy Inputs

A policy decision SHOULD evaluate:

- actor identity
- agent identity
- tenant
- contract
- intent
- action
- target
- requested data scope
- requested tool scope
- requested memory scope
- requested time window
- risk level
- obligations

## Policy Outcomes

A resolver MUST return one of:

- allow
- deny
- allow_with_redaction
- allow_with_human_approval
- allow_with_obligations
- deny_with_reason

## Policy Evidence

A signed context packet SHOULD include policy evidence or references:

```yaml
policy:
  decision: allow_with_redaction
  engine: opa
  policy_id: acp.customer_support.read
  policy_hash: sha256:placeholder
  evaluated_at: "2026-06-09T00:00:00Z"
```

## Denial Rule

When policy denies a request, the resolver MUST NOT assemble context.

## Redaction Rule

When policy allows with redaction, the resolver MUST redact before signing the context packet.

## Approval Rule

When policy requires human approval, the resolver MUST NOT issue a usable context packet until approval is recorded.

## Compatibility

ACP policy evaluation may be implemented using systems such as OPA, OpenFGA, AuthZEN-compatible APIs, custom policy engines, or native database access policies.

ACP does not require a specific engine. ACP requires observable policy enforcement.
