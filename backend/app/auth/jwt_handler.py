from datetime import datetime, timedelta
import jwt

SESCRET_KEY = "kjgkajaskfskdlf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 60

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRES_MINUTES
    )

    return jwt.encode(payload, SESCRET_KEY, algorithm=ALGORITHM)

def decoded_token(token: str):
    return jwt.decode(token, SESCRET_KEY, algorithms=[ALGORITHM])