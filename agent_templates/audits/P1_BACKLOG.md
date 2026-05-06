# P1 Safety Backlog

| Path | Risk | Recommendation |
| :--- | :--- | :--- |
| CLI_router.py | Writes unverified Python code to skill paths. | Add human confirmation gate before file write. |
| memory_manager.py | Hardcoded absolute paths to hnxj-gemini. | Use relative paths or environment variables. |
| policy_optimizer.py | Hardcoded absolute paths to ~/.gemini. | Use relative paths or environment variables. |
| warehouse_manager.py | Hardcoded absolute paths and broad migration logic. | Narrow scope and add validation checks. |
| infrastructure/mlx_offline_router.py | Local model execution surface. | Add explicit usage warnings and VRAM monitoring. |
| local_toggle.py | Dummy key assignment (benign but confusing). | Remove dummy key or clearly label as mock. |

[gemini-cli-pro][/Users/hamednejat/gemini-gamma-labyrinth-clean/repos][20260506-1830]
