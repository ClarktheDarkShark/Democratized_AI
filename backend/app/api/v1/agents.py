from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...core.auth import require_roles
from ...core.deps import get_db
from ...domain import models, schemas

router = APIRouter(prefix="/agents", tags=["agents"])

@router.post("", response_model=schemas.AgentRead, dependencies=[Depends(require_roles(["builder", "admin"]))])
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    obj = models.Agent(**agent.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=List[schemas.AgentRead], dependencies=[Depends(require_roles(["builder", "operator", "admin"]))])
def list_agents(db: Session = Depends(get_db)):
    return db.query(models.Agent).all()
