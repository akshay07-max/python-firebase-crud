import requests
from firebase_admin import auth
from auth.jwt_handler import create_access_token

FIREBASE_API_KEY = "YOUR_FIREBASE_API_KEY"

def login_user(email:str, password:str):
    url=("https://identitytoolkit.googleapis.com/v1/"f"accounts:signInWithPassword?key={FIREBASE_API_KEY}")

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    res = requests.post(url, json=payload)

    if res.status_code != 200:
        raise Exception("Invalid Credentials")
    
    firebase_token= res.json()["idToken"]
    decoded = auth.verify_id_token(firebase_token)

    access_token = create_access_token({
        "uid": decoded["uid"],
        "email": decoded["email"],
        "role": decoded.get("role")
    })

    return access_token
