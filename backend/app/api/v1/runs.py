from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...core.auth import require_roles
from ...core.deps import get_db
from ...domain import models, schemas

router = APIRouter(prefix="/runs", tags=["runs"])

@router.post("", response_model=schemas.RunRead, dependencies=[Depends(require_roles(["operator", "admin"]))])
def start_run(run_in: schemas.RunCreate, db: Session = Depends(get_db)):
    run = models.Run(agent_id=run_in.agent_id, status=models.RunStatus.pending, input=run_in.input)
    db.add(run)
    db.commit()
    db.refresh(run)
    return run

@router.get("", response_model=List[schemas.RunRead], dependencies=[Depends(require_roles(["operator", "admin", "approver"]))])
def list_runs(status: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(models.Run)
    if status:
        q = q.filter(models.Run.status == status)
    return q.all()

@router.get("/{run_id}", response_model=schemas.RunRead, dependencies=[Depends(require_roles(["operator", "admin", "approver"]))])
def get_run(run_id: int, db: Session = Depends(get_db)):
    return db.get(models.Run, run_id)
