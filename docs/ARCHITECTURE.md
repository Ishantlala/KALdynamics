# System Architecture — Project FAChealth

## Hybrid Edge-Cloud Pipeline
1. **01 · Machine Sensors (Input):** Retrofits onto existing PLC/factory sensors capturing vibration (`mm/s`), temperature (`C`), pressure (`bar`), and current (`A`).
2. **02 · Edge Gateway (Edge Linux + Python + MQTT):** Performs sub-second signal filtering, rolling-window anomaly flagging, and local disk ring-buffering so temporary network drops never lose fault telemetry.
3. **03 · FAChealth Cloud Server (FastAPI + TimescaleDB + ML):** Stores normalized time-series streams in TimescaleDB hypertables, runs Isolation Forest anomaly confirmation, and computes Remaining Useful Life (RUL) windows using PyTorch.
4. **04 · MCP Orchestration & RBAC Console (MCP + React/TypeScript):** Translates high-risk RUL predictions into actionable maintenance workflows—checking spare-part inventory, drafting CMMS work orders/PRs, and attaching Lockout-Tagout (LOTO) safety SOPs before pausing for authorized engineer approval.

## OT Security & Governance
* **Transport & Identity:** Per-gateway X.509 device certificates over encrypted MQTT/TLS.
* **No Blind Actuation:** Critical work orders, purchase requisitions, and line-interlock actions strictly require verified RBAC sign-off with timestamped audit logs.
