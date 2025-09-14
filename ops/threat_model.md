# Threat Model (STRIDE)

| Threat | Mitigation |
|-------|------------|
| Spoofing | JWT auth with roles |
| Tampering | Hash-chained audit logs |
| Repudiation | Structured logging and approvals |
| Information Disclosure | DLP stubs and allow-lists |
| Denial of Service | Rate limiting (future) |
| Elevation of Privilege | RBAC and policy engine |
