# Agent Instructions: Security Audit Framework

As an AI agent assisting with this repository, you are responsible for
maintaining the **Security-Audit-MCP** architecture.

## 🛡️ Core Responsibilities

1. **Maintain the Manifest:** Any change that addresses a security control
   (OWASP, NIST, etc.) must be documented in `security-map.json`.
2. **Artifact Integrity:** Ensure all files listed in `security-map.json`
   exist and are correctly mapped to their respective controls.
3. **Proactive Auditing:** Before submitting any change, run the automated
   security auditor to ensure no regressions (like deprecated links or
   insecure URLs) were introduced.

## 🛠️ Tooling

### Security Auditor

Run the custom Python auditor to validate the project's security posture:

```bash
python3 scripts/security_auditor.py
```

### CI/CD Emulation

To simulate the full security pipeline locally:

* **Links:** `lychee README.md`
* **Secrets:** `gitleaks detect --source . -v`
* **Linting:** `markdownlint-cli2 "**/*.md"`

## 📝 Markdown Standards

All documentation must adhere to strict formatting to pass CI:

* No inline HTML (`<div>`, `<a>`, `<img>`, etc.).
* Mandatory alt-text for all images.
* First line must be a top-level H1 heading.
* **80-character line limit** for text. Use reference-style links at the
  bottom of the file for long URLs.

## 📌 Update Procedure

When adding a new feature or project:

1. Add the project to the "Featured Project" or "Tech Stack" in `README.md`.
2. Update `security-map.json` with relevant controls and artifacts.
3. Verify that `scripts/security_auditor.py` passes.
