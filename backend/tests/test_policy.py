from fastapi.testclient import TestClient

from app.main import app
from app.core import auth

client = TestClient(app)

def test_policy_denied():
    token = auth.create_token("u", "builder")
    resp = client.post("/tools/execute", json={"tool": "calculator", "args": {"expression": "1+1"}}, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403
