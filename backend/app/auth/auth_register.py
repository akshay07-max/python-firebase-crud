from firebase_admin import auth
from firebase_setup import db

def register_user(email: str, password:str, role: str):
    user = auth.create_user(
        email=email,
        password=password
    )

    # storing role
    auth.set_custom_user_claims(
        user.uid,
        {"role": role}
    )

    # store user profile
    db.collection("users").document(user.uid).set({
        "email":email,
        "role": role,
        "active": True
    })

    return user.uid

