from typing import List, Dict
from sqlalchemy.orm import Session

from ...domain import models


def query(db: Session, query: str, top_k: int = 5) -> List[Dict[str, str]]:
    docs = db.query(models.Document).limit(top_k).all()
    return [{"text": query, "source": d.uri or str(d.id)} for d in docs]
