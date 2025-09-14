from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...core.auth import require_roles
from ...core.deps import get_db
from ...services.rag import ingest, retrieve

router = APIRouter(prefix="/rag", tags=["rag"])

@router.post("/ingest", dependencies=[Depends(require_roles(["builder", "admin"]))])
def ingest_docs(texts: List[str], db: Session = Depends(get_db)):
    ids = ingest.ingest_texts(db, texts)
    return {"ids": ids}

@router.post("/query", dependencies=[Depends(require_roles(["operator", "admin"]))])
def query_docs(query: str, db: Session = Depends(get_db)):
    passages = retrieve.query(db, query)
    return {"passages": passages}
