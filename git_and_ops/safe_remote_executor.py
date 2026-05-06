"""DEPRECATED_P0_UNSAFE_TOOL.

This script is intentionally disabled in Gamma Labyrinth agent commons.
Reason: Provides an open wrapper for arbitrary SSH/SCP remote execution.
Use the Tool Risk Audit process before any redesign.
"""

from __future__ import annotations

def main() -> int:
    print("DEPRECATED_P0_UNSAFE_TOOL: disabled by default. See agent_templates/audits/safe_remote_executor.md")
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
