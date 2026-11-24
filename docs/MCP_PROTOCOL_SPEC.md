# MCP Protocol Specification — Project FAChealth

Project FAChealth uses the **Model Context Protocol (MCP)** to turn passive predictive alerts into safe, closed-loop repair coordination across industrial software systems.

## Modular MCP Servers

| Server | Responsibility | Approval Gate |
| :--- | :--- | :--- |
| `telemetry-mcp` | Read-only access to live machine snapshots, anomaly history, and RUL forecasts | Autonomous (Read-Only) |
| `cmms-inventory-mcp` | Checks spare-part stock levels; drafts work orders and purchase requisitions; dispatches approved tickets | Drafts Autonomous / Dispatch Requires RBAC Approval |
| `sop-safety-mcp` | Retrieves asset-specific repair checklists and verifies Lockout-Tagout (LOTO) safety prerequisites | Autonomous (Read-Only) / Sign-Off Logged |

## Closed-Loop Execution Flow
1. `telemetry-mcp` surfaces an anomaly where `predicted_rul_hours < 24` and confidence exceeds threshold.
2. `cmms-inventory-mcp` queries spare inventory for the affected component (e.g., `BRG-6208-2RS`) and drafts a work order + PR if stock is below reorder level.
3. `sop-safety-mcp` binds the exact asset maintenance checklist and safety SOP to the draft ticket.
4. The orchestrator pauses execution and pushes an approval card to the React RBAC console.
5. Upon engineer approval, `cmms-inventory-mcp` commits the work order/PR and writes an immutable audit record.
