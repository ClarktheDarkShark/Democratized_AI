from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel

class AgentCreate(BaseModel):
    name: str
    config: Dict[str, Any]

class AgentRead(AgentCreate):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class RunCreate(BaseModel):
    agent_id: int
    input: Dict[str, Any] | None = None

class RunRead(BaseModel):
    id: int
    agent_id: int
    status: str
    input: Dict[str, Any] | None
    output: Dict[str, Any] | None
    created_at: datetime
    class Config:
        orm_mode = True

class ApprovalCreate(BaseModel):
    run_id: int
    payload: Dict[str, Any]

class ApprovalDecision(BaseModel):
    decision: str

class ApprovalRead(BaseModel):
    id: int
    run_id: int
    status: str
    payload: Dict[str, Any] | None
    class Config:
        orm_mode = True
