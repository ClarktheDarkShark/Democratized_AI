from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_serves_landing_page():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Agentic Platform API" in resp.text
