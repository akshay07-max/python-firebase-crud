from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from auth.jwt_handler import decoded_token

security = HTTPBearer()

def get_current_user(creds=Depends(security)):
    try:
        return decoded_token(creds.credentials)
    
    except Exception:
        raise HTTPException(401, "Invalid Token")
    
