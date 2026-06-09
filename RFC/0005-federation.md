# RFC 0005: ACP Federation

Status: Draft  
Version: v0.1

## Summary

ACP federation defines how context can be requested, authorized, exchanged, and audited across domains, tenants, organizations, clouds, and agent runtimes.

Federation does not mean open context sharing. Federation means governed cross-domain context exchange.

## Core Concepts

### ACP Domain

An ACP Domain is a bounded administrative, organizational, tenant, cloud, or runtime boundary that controls context resolution.

### ACP Resolver

An ACP Resolver evaluates context requests and issues signed context packets.

### ACP Trust Anchor

A Trust Anchor is an identity, key, organization, or registry entry trusted to verify ACP domain or resolver identity.

### ACP Federation Gateway

A Federation Gateway mediates context exchange between ACP domains.

### ACP Trust Chain

A Trust Chain is verifiable evidence connecting actor identity, agent identity, contract, policy, resolver, packet, and audit record.

### ACP Audit Chain

An Audit Chain links context request, policy decision, packet issuance, execution, expiry, and post-execution evidence.

## Federation Rule

No cross-domain context without:

- identity trust
- contract trust
- policy trust
- resolver trust
- audit trust

## Cross-Domain Flow

1. Requesting domain submits a scoped context request.
2. Receiving domain verifies requesting domain identity.
3. Receiving domain verifies actor and agent claims.
4. Receiving domain verifies contract or delegation.
5. Receiving domain evaluates local policy.
6. Receiving domain applies redaction and obligations.
7. Receiving domain issues a signed context packet or denial.
8. Both domains record audit evidence.

## Default Deny

Cross-domain context exchange MUST be denied by default.

## Tenant Boundary

Federation MUST NOT weaken tenant isolation.

## Delegation

Delegation SHOULD be explicit, time-bounded, signed, and auditable.

## Non-Goals

ACP v0.1 federation does not define a global registry, universal trust root, mandatory PKI, or single vendor control plane.
