# Agent Update Ledger Template

**Purpose:** Provide a compact, parseable, and standardized format for agents to leave status updates and handoff notes in shared channels or coordination issues, without polluting the execution layer or leaking secrets.

**Instructions for Agents:**
1. Copy this template.
2. Fill in the fields accurately for your current execution turn.
3. Post as a comment in the designated GitHub Coordination Issue or shared log.
4. **Never** include tokens, PATs, or `.env` secrets.
5. **Never** claim scientific truth unless referencing a validated Truth-plane receipt.

---

### [Agent Update: YYYYMMDD-HHMM]

**Agent/Model:** `<e.g., Gemini CLI Flash Lite>`
**Workspace Root:** `<e.g., /Users/name/gemini-gamma-labyrinth-clean/repos>`
**Target Repo:** `<e.g., gamma-tools>`
**Active Branch:** `<e.g., main>`

**Task Objective:** `<Brief 1-sentence summary of the goal>`
**Plane:** `<Control | Execution | Observation | Analysis | Science | Social>`

**Status:** `[PASS | PARTIAL | BLOCKED | FAILED]`
**Truth Mode:** `[truth_safe_unverified | truth_verified_receipt]`

**Actions Performed:**
- `<List key commands run or API calls made>`

**Files Changed:**
- `<List exact file paths modified>`

**Identified Risks/Blockers:**
- `<List any supply chain, security, or coordination risks encountered>`

**Next Safe Action (Handoff):**
- `<State exactly ONE concrete action the next agent or human should take>`

---
