from fastapi import Request

from .logging import logger

async def audit_middleware(request: Request, call_next):
    response = await call_next(request)
    logger.info("audit", extra={"path": request.url.path, "method": request.method, "user": request.headers.get('authorization')})
    return response
