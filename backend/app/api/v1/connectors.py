from fastapi import APIRouter, Depends, HTTPException

from ...core.auth import require_roles
from ...services.connectors.filesystem import FilesystemConnector
from ...services.connectors.http_api import HTTPAPIConnector
from ...services.connectors.sharepoint_mock import SharePointConnector

router = APIRouter(prefix="/connectors", tags=["connectors"])

CONNECTORS = {
    "filesystem": FilesystemConnector(),
    "http_api": HTTPAPIConnector(),
    "sharepoint": SharePointConnector(),
}

@router.post("/test", dependencies=[Depends(require_roles(["builder", "admin"]))])
def test_connector(type: str, config: dict):
    connector = CONNECTORS.get(type)
    if not connector:
        raise HTTPException(status_code=404, detail="unknown connector")
    return {"ok": connector.test(config)}
