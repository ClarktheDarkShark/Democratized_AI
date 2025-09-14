import time
from typing import List

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from .config import settings

class TokenData(BaseModel):
    sub: str
    role: str

security = HTTPBearer()

def create_token(sub: str, role: str) -> str:
    payload = {"sub": sub, "role": role, "iat": int(time.time())}
    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")

def decode_token(token: str) -> TokenData:
    try:
        data = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        return TokenData(**data)
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    return decode_token(credentials.credentials)

def require_roles(roles: List[str]):
    def wrapper(user: TokenData = Depends(get_current_user)) -> TokenData:
        if user.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return user
    return wrapper
