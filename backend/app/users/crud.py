from firebase_setup import db

def get_profile(uid: str):
    doc = db.collection("users").document(uid).get()
    return doc.to_dict()

