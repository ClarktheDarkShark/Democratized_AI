from sqlalchemy.orm import Session

from ...domain import models


def request_approval(db: Session, run_id: int, payload: dict) -> models.Approval:
    approval = models.Approval(run_id=run_id, payload=payload)
    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval
