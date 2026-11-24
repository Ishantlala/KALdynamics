# 24-Hour Hackathon MVP Roadmap & Risk Plan

## Build Split (Team KALdynamics)
* **Hours 0–6 (Telemetry & Edge Replay):** Build fault-injection telemetry replay stream, local edge filtering, MQTT ingestion, and TimescaleDB schema.
* **Hours 6–14 (ML + MCP Core):** Wire Isolation Forest anomaly scoring + RUL estimator in FastAPI and implement `telemetry-mcp`, `cmms-inventory-mcp`, and `sop-safety-mcp`.
* **Hours 14–20 (Operator Console & RBAC):** Build React + TypeScript dashboard showing live telemetry replay, anomaly feed, drafted work orders/PRs, SOP checklists, and role-verified approval buttons.
* **Hours 20–24 (Validation & Demo):** Run end-to-end fault-injection scenarios, verify offline edge buffer recovery, and rehearse live demo.

## Risks & Mitigations
* **Sparse Real Fault Data:** Train and validate initial baselines using structured fault-injection datasets.
* **False Alarms / Alert Fatigue:** Combine statistical confidence thresholds with mandatory engineer review before dispatching parts or line stops.
* **Industrial OT Security:** Isolate sensor networks behind authenticated edge gateways with TLS encryption and device certificates.

## Commercial Path
* **Target Customers:** Discrete and process manufacturers (mid-to-large factories, automotive lines, industrial OEMs).
* **Go-To-Market:** 90-day single-line pilot in Bengaluru industrial clusters to prove downtime ROI, scaling to per-machine B2B SaaS + Edge Gateway licensing.
