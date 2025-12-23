from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

security = HTTPBearer()
SECRET = os.getenv("JWT_SECRET", "secret")

def create_token():
    return jwt.encode({"user": "guest"}, SECRET, algorithm="HS256")

def verify_token(
    cred: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        jwt.decode(cred.credentials, SECRET, algorithms=["HS256"])
        return cred.credentials
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
