from fastapi import FastAPI, Depends
from dependencies import firebase_auth
from firebase_setup import db

app = FastAPI()

# protected route
@app.get("/profile")
def get_profile(user=Depends(firebase_auth)):
    uid = user["uid"]

    doc = db.collection("users").document(uid).get()

    return doc.to_dict()

