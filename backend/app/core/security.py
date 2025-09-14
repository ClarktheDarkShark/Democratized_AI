from typing import Any, Dict

from fastapi import HTTPException, status

from .auth import TokenData

ALLOWED_TOOLS = {"calculator", "http_get", "iac_emitter"}


def policy_check(subject: TokenData, action: str, resource: Dict[str, Any], context: Dict[str, Any] | None = None) -> None:
    if subject.role == "admin":
        return
    if action == "tools.execute" and resource.get("tool") in ALLOWED_TOOLS and subject.role in {"operator", "builder"}:
        return
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="policy_denied")


def dlp_scan(text: str) -> bool:
    return "SSN" in text  # very naive placeholder
