# Modular MCP Servers

Each domain toolset is isolated as an independent MCP server managed by the FAChealth orchestrator:
* `telemetry-mcp/`: Machine health snapshots, anomaly event logs, and RUL predictions.
* `cmms-inventory-mcp/`: Spare-part stock checks, CMMS work order drafting, PR creation, and RBAC-gated dispatch.
* `sop-safety-mcp/`: Asset-specific repair checklists and Lockout-Tagout (LOTO) safety verification.

See `../schemas/mcp_tools_manifest.json` for full tool definitions and approval gates.
