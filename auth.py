from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError


class Authentication:

    def __init__(self, cfg: dict):
        self.__cfg = cfg

    def auth(self, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
            )
        decoded = self.decode_token(token)
        # decoded = token
        if not decoded:
            raise credentials_exception
        return decoded

    def encode_token(self, username:str, expires_delta:Optional[timedelta] = None  ):
        if expires_delta:
            expire = (datetime.now(timezone.utc) + expires_delta).isoformat()
        else:
            expire = (datetime.now(timezone.utc) + timedelta(minutes=int(self.__cfg["JWT_EXPIRE"]))).isoformat()

        return jwt.encode({
            "user" : username, 
            "expire": expire
            }, key=self.__cfg["JWT_SECRET"], algorithm=self.__cfg["JWT_ALGO"])
        

    def decode_token(self, token: str) -> dict |None:
        try:
            payload = jwt.decode(token, self.__cfg["JWT_SECRET"], algorithms=[self.__cfg["JWT_ALGO"]])
            if any(x not in payload for x in ["user", "expire"]):
                return None
            return payload
        except InvalidTokenError:
            return None



