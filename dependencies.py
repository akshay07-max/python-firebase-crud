from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth

sercurity = HTTPBearer()

def firebase_auth(creds: HTTPAuthorizationCredentials = Depends(sercurity)):
    try:
        token = creds.credentials
        decoded = auth.verify_id_token(token)
        return decoded
    
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized"
        )