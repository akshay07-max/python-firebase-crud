from fastapi import FastAPI, Depends
from auth.register import register_user
from auth.login import login_user
from auth.login import logout_user
from auth.dependencies import get_current_user
from users.crud import get_profile

app = FastAPI()

@app.post("/register")
def register(data: str)
    uid = register_user(
        data["email"],
        data["password"],
        data["role"]
    )
    return {"uid": uid}

@app.post("/login")
def login(data: dict):
    token = login_user(data["email"], data["password"])
    return {"access_token": token}