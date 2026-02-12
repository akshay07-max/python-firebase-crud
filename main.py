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

# to create a profile.
@app.post("/profile")
def create_profile(data: dict, user=Depends(firebase_auth)):
    uid=user["uid"]

    db.collection("users").document(uid).set({
        **data,
        "email": user.get("email"),
        "active": True
    })

    return {"status":"profile Created"}