from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel



class Authentication:

    def __init__(self, cfg: dict):
        self.__cfg = cfg

    def auth(self, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
            )
        # decoded = self.decode_token(token)
        decoded = token
        if not decoded:
            raise credentials_exception
        return decoded

    def encode_token(self, username:str, expires_delta:Optional[timedelta] = None  ):
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=int(self.__cfg["JWT_EXPIRE"]))

        return jwt.encode({
            "user" : username,
            "id" : id,
            "expire": expire
            }, key=self.__cfg["JWT_SECRET"], algorithm=self.__cfg["JWT_ALGO"])
        

    def decode_token(self, token: str) -> dict |None:
        try:
            payload = jwt.decode(token, self.__cfg["JWT_SECRET"], algorithms=[self.__cfg["JWT_ALGO"]])
            # if something
            return payload
        except InvalidTokenError:
            return None



