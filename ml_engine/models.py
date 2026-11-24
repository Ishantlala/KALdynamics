from pydantic import BaseModel, Field
from typing import Literal, Optional


class SensorReading(BaseModel):
    machine_id: str
    plant_id: str
    vibration_mm_s: float
    temperature_c: float
    pressure_bar: float
    current_a: float


class HealthEvaluation(BaseModel):
    machine_id: str
    anomaly_detected: bool
    confidence: float = Field(ge=0.0, le=1.0)
    predicted_rul_hours: float
    recommended_part_sku: Optional[str] = None
    requires_human_approval: bool


class RBACApprovalDecision(BaseModel):
    action_id: str
    action_type: Literal["dispatch_work_order", "submit_purchase_requisition", "verify_loto"]
    approver_id: str
    approver_role: Literal["maintenance_engineer", "plant_manager", "safety_lead"]
    approved: bool
    notes: Optional[str] = None
