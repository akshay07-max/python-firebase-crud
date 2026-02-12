import requests
from firebase_admin import auth
from auth.jwt_handler import create_access_token

FIREBASE_API_KEY = "YOUR_FIREBASE_API_KEY"