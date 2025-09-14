from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...core.auth import require_roles
from ...core.deps import get_db
from ...domain import models, schemas

router = APIRouter(prefix="/approvals", tags=["approvals"])

@router.get("", dependencies=[Depends(require_roles(["approver", "admin"]))])
def list_approvals(db: Session = Depends(get_db)):
    return db.query(models.Approval).all()

@router.post("/request", response_model=schemas.ApprovalRead, dependencies=[Depends(require_roles(["operator", "admin"]))])
def request_approval(data: schemas.ApprovalCreate, db: Session = Depends(get_db)):
    approval = models.Approval(run_id=data.run_id, payload=data.payload, status="pending")
    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval

@router.post("/{approval_id}/decide", dependencies=[Depends(require_roles(["approver", "admin"]))])
def decide(approval_id: int, decision: schemas.ApprovalDecision, db: Session = Depends(get_db)):
    approval = db.get(models.Approval, approval_id)
    approval.status = decision.decision
    db.commit()
    return {"status": approval.status}
