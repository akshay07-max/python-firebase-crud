from firebase_setup import db

def get_profile(uid: str):
    doc = db.collection("users").document(uid).get()
    return doc.to_dict()

def update_profile(uid: str, data: dict):
    db.collection("users").document(uid).update(data)

def delete_profile(uid:str):
    db.collection("users").document(uid).delete()

