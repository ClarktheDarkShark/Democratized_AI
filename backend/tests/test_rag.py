from fastapi.testclient import TestClient

from app.main import app
from app.core import auth

client = TestClient(app)

def test_rag_flow():
    token_builder = auth.create_token("u", "builder")
    r = client.post("/rag/ingest", json=["hello world"], headers={"Authorization": f"Bearer {token_builder}"})
    assert r.status_code == 200
    token_operator = auth.create_token("u", "operator")
    q = client.post("/rag/query", json="hello", headers={"Authorization": f"Bearer {token_operator}"})
    assert q.status_code == 200
