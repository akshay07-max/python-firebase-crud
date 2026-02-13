from fastapi import FastAPI, Depends
from auth.register import register_user
from auth.login import logout_user
from auth.dependencies import get_current_user
from users.crud import get_profile

app = FastAPI()

