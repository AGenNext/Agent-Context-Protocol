# Security Policy

## Status

ACP is currently published as Draft v0.1 for review.

## Security Model

ACP assumes that agent runtimes, tools, memory systems, and context stores may be misconfigured, over-permissive, or exposed to prompt injection and confused-deputy behavior.

ACP therefore treats context as privileged runtime material.

## Required Security Controls

ACP-compatible implementations SHOULD enforce:

- actor identity verification
- agent identity verification
- contract verification
- policy evaluation before context assembly
- least-context delivery
- tenant boundary enforcement
- redaction before packet signing
- signed context packets
- packet expiry
- replay prevention
- audit record creation
- denial logging
- secure key management
- revocation support

## Sensitive Data

Context packets MUST NOT include secrets, credentials, payment data, private memory, or cross-tenant records unless explicitly allowed by contract and policy.

## Replay Protection

A packet MUST NOT be reused after expiry or for a different actor, agent, action, target, tenant, or contract.

## Reporting Security Issues

Please open a private security advisory or contact the maintainers before public disclosure.

Do not include live secrets, production credentials, customer data, or private tenant data in public issues.
