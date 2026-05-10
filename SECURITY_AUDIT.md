# 🛡️ Security Audit Handbook

This document outlines how automated security audits are structured and executed for this profile and related projects.

## 🏗️ Knowledge Architecture

To enable efficient, automated audits (like OWASP Top 10 or NIST CSF) by AI agents or CI/CD pipelines without overwhelming the context window, we use a **Structured Security Manifest**.

### 1. Security Manifest (`security-map.json`)
The `security-map.json` file serves as the primary index. It maps specific compliance controls to the codebases or documentation artifacts that satisfy them.

*   **Benefit:** Agents can query this file to understand *where* to look for evidence of a specific control (e.g., "Where is encryption implemented?").

### 2. Automated CI/CD Pipeline
Every change to this repository triggers an automated security scan defined in `.github/workflows/security-pipeline.yml`.

*   **🔗 Link Integrity:** Uses `lychee` to ensure no broken or deprecated URL shorteners (like `git.io`) are used.
*   **🔐 Secret Scanning:** Uses `gitleaks` to detect accidentally committed credentials.
*   **📝 Quality Assurance:** Uses `markdownlint` to maintain documentation standards.

## 🚀 How to Run an Audit

### Automated (CI/CD)
The audit runs automatically on every Pull Request. Review the "Actions" tab in GitHub to see the status of:
- `Security Scan` (Lychee, Gitleaks, Markdownlint)
- `Compliance Mapping` (Manifest Validation)

### Local Manual Audit
If you have the tools installed, you can simulate the CI audit locally:

```bash
# Link check
lychee README.md

# Secret scan
gitleaks detect --source . -v

# Manifest validation
jq . security-map.json
```

## 📜 Compliance Coverage
The current mapping in `security-map.json` covers:
- **OWASP Top 10 (2021)**: Focused on A02, A05, and A06.
- **NIST CSF v1.1**: Focused on ID.AM, PR.DS, and DE.CM.

---
*Maintained by Nasima | Cybersecurity + AI = 🛡️ Sentinel AI*
