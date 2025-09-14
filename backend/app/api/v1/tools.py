from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ...core.auth import TokenData, require_roles
from ...core.security import policy_check
from ...services.tools.calculator import CalculatorTool
from ...services.tools.http_get import HTTPGetTool
from ...services.tools.iac_emitter import IacEmitterTool

router = APIRouter(prefix="/tools", tags=["tools"])

TOOLS = {
    "calculator": CalculatorTool(),
    "http_get": HTTPGetTool(),
    "iac_emitter": IacEmitterTool(),
}

class ToolRequest(BaseModel):
    tool: str
    args: dict

@router.post("/execute")
def execute(req: ToolRequest, user: TokenData = Depends(require_roles(["operator", "admin"]))):
    policy_check(user, "tools.execute", {"tool": req.tool})
    t = TOOLS.get(req.tool)
    if not t:
        raise HTTPException(status_code=404, detail="unknown tool")
    return {"result": t.execute(req.args)}
