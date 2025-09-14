from typing import List
from sqlalchemy.orm import Session

from ...domain import models


def ingest_texts(db: Session, texts: List[str]) -> List[int]:
    ids = []
    for text in texts:
        doc = models.Document(source="upload", uri="", meta={})
        db.add(doc)
        db.flush()
        emb = models.Embedding(document_id=doc.id, chunk_id=0, vector=str([0.0]))
        db.add(emb)
        ids.append(doc.id)
    db.commit()
    return ids
