from firebase_setup import db

def batch_write_users(users: list):
    batch = db.batch()

    for user in users:
        ref = db.collection("users").document(user["id"])
        batch.set(ref, user["data"])

    batch.commit()