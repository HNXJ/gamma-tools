# Tool Risk Audit Template

**Purpose:** Provide a bounded, inspectable, agent-readable format for evaluating any new tool, extension, package, or integration before it is adopted into the Gamma Labyrinth agent commons. Covers Gemini CLI extensions, MCP servers, CLI tools, Python packages, browser/devtools integrations, GitHub apps, cloud integrations, and local telemetry utilities.

**Instructions for Agents:**
1. Copy this template into a coordination issue, PR description, or `agent_templates/audits/<tool-slug>.md` working file.
2. Fill in every field; mark `n/a` only when genuinely not applicable, never to skip a check.
3. Treat unknown values as risk, not as silent acceptance.
4. **Never** include tokens, PATs, API keys, `.env` contents, bearer strings, or private keys in this audit. Reference their *expected location* only.
5. **Never** assert biological or runtime truth in this template — Truth-plane state requires a validated `gamma` receipt.
6. **Never** install, run, or auto-adopt a tool from inside the audit document. Adoption requires a separate, explicitly authorized execution turn.
7. The audit is doctrine; it is not a runtime artifact.

---

### [Tool Risk Audit: YYYYMMDD-HHMM UTC]

**Header:** `[model-llm-name][root-location][YYYYMMDD-HHMM]`

#### 1. Tool Identity

- **Name:** `<canonical name>`
- **Source URL:** `<repo / package registry / vendor docs>`
- **Maintainer:** `<org or individual; official vs community>`
- **Version / Ref / Tag / Commit:** `<pinned ref if available>`
- **Package Registry:** `<npm | PyPI | crates.io | GitHub Releases | n/a>`
- **Last Verified Date (UTC):** `<YYYYMMDD>`
- **Reviewer Identity:** `<agent tag, e.g., claude_cowork>`

#### 2. Classification

Mark exactly one primary class; add secondaries if needed.

- [ ] Gemini CLI extension
- [ ] MCP server
- [ ] CLI tool
- [ ] Python package
- [ ] Browser / devtools integration
- [ ] Cloud integration
- [ ] Local telemetry / observability
- [ ] Other: `<describe>`

#### 3. Gamma Plane Fit

Where this tool is allowed to operate. Cross-plane operation requires explicit doctrine review.

- [ ] Control (doctrine, planning, routing)
- [ ] Execution (orchestration, code, simulation)
- [ ] Truth (receipt-gated state) — requires extra scrutiny
- [ ] Observation (dashboards, public views)
- [ ] Analysis (derived reports)
- [ ] Science source (references, grounding)
- [ ] Agent commons (`gamma-tools`)

#### 4. Permission Surface

- [ ] Filesystem read
- [ ] Filesystem write
- [ ] Shell / process execution
- [ ] Network egress
- [ ] Browser / session access
- [ ] GitHub / Git API
- [ ] Cloud provider API
- [ ] Local model endpoint
- [ ] Database access
- [ ] Secrets / auth material

State the *narrowest* surface needed for the intended use; flag anything broader as supply-chain risk.

#### 5. Secret Handling

- **Auth required:** `[ yes | no ]`
- **Where token is expected:** `<env var name | OS keychain | n/a>`
- **Forbidden storage locations:** workspace `.env` files, repo-tracked config, agent memory files (`GEMINI.md`, `CLAUDE.md`, etc.), issue comments, transcripts, this audit document.
- **Redaction behavior:** `<does the tool redact secrets in logs/errors? cite source>`
- **Least-privilege scope possible:** `[ yes | no | unknown ]` — describe scope.

#### 6. Supply-Chain Risk

- [ ] Source is official / maintainer-published
- [ ] Source is third-party / community fork
- [ ] Source is inspectable (open source, published tarball)
- [ ] Pinned ref / tag / SHA available
- [ ] Releases / changelog available
- [ ] Install command is transparent (no `curl | bash`, no opaque installer)
- [ ] No known typosquat / impersonation risk on the registry
- **Notes:** `<describe any supply-chain anomalies>`

#### 7. Runtime Risk

- [ ] Can mutate local files
- [ ] Can push / merge / delete in Git or GitHub
- [ ] Can run arbitrary shell
- [ ] Can access browser / authenticated session
- [ ] Can access local model endpoints
- [ ] Can access cloud data
- [ ] Can mutate Truth-plane state in `gamma` (receipts, persistence)
- [ ] Can exfiltrate data (network egress + secret access)
- **Blast radius if compromised:** `<describe>`

#### 8. Evidence Required Before Adoption

- [ ] Documentation / source links recorded above
- [ ] Install manifest captured (exact command, exact ref)
- [ ] Permissions enumerated and minimized
- [ ] Sandbox test performed in an isolated environment
- [ ] No-secret proof: grep / scan confirms no secrets touched
- [ ] Rollback plan documented (uninstall, revert, revoke)
- [ ] Logs / artifacts saved with hashes
- [ ] Reviewer identity recorded (agent + model + role)

#### 9. Recommendation Rubric

Choose exactly one verdict; justify in one sentence.

- [ ] `ADOPT_NOW_READONLY` — read-only, narrow scope, official source, pinned ref, no secret access.
- [ ] `PILOT_SANDBOX` — promising but warrants a bounded sandbox trial with logging before broader use.
- [ ] `CUSTOM_GAMMA_EXTENSION` — capability is needed, but a Gamma-native, doctrine-aligned implementation is safer than the third-party tool.
- [ ] `DEFER` — incomplete evidence; revisit after listed gaps are closed.
- [ ] `REJECT_UNVERIFIED_OR_RISKY` — fails one or more stop conditions.

**Verdict:** `<one of the above>`
**One-sentence justification:** `<why>`

#### 10. Stop Conditions (any one triggers `REJECT_UNVERIFIED_OR_RISKY`)

- Opaque installer (`curl | bash`, anonymous binary, unsigned blob).
- Hardcoded secret in source, config, or example.
- Broad write access requested without functional need.
- Force-push or branch-delete automation enabled by default.
- Any path that could mutate Truth-plane state without a `gamma` receipt.
- Any unverified biological or scientific claim embedded in the tool's defaults.
- Source missing, deleted, or maintainer unverifiable.
- No documented rollback / uninstall procedure.

#### 11. Final Audit Report

Copy this block into the coordination issue when the audit is complete.

```
[model-llm-name][root-location][YYYYMMDD-HHMM]

Tool: <name @ ref>
Classification: <primary class>
Gamma Plane Fit: <planes>
Reviewer: <agent tag>
Truth Mode: truth_safe_unverified

Permission Surface (narrowest needed): <list>
Supply-Chain Risk: <summary>
Runtime Risk: <summary>
Stop Conditions Hit: <none | list>

Verdict: <ADOPT_NOW_READONLY | PILOT_SANDBOX | CUSTOM_GAMMA_EXTENSION | DEFER | REJECT_UNVERIFIED_OR_RISKY>
Justification: <one sentence>

Evidence Artifacts:
- <links / hashes / sandbox logs>

Next Safe Action:
- <one concrete step>

[model-llm-name][root-location][YYYYMMDD-HHMM]
```

---

**Footer:** `[model-llm-name][root-location][YYYYMMDD-HHMM]`
