from firebase_setup import db

def batch_write_users(users: list):
    batch = db.batch()

    for user in users:
        ref = db.collection("users").document(user["id"])
        batch.set(ref, user["data"])

    batch.commit()

def batch_delete_users(user_ids: list):
    batch = db.batch()

    for uid in user_ids:
        ref = db.collection("users").document(uid)
        batch.delete(ref)

    batch.commit()


def get_active_users():
    users = (
        db.collection("users")
        .where("active", "==", True)
        .stream()
    )

    return [u.to_dict() for u in users ]

def get_latest_users(limit: int = 5):
    users = (
        db.collection("users")
        .order_by("created_at", direction="DESCENDING")
        .limit(limit)
        .stream()
    )
    return [u.to_dict() for u in users]


def search_by_name(prefix: str):
    users = (
        db.collection("users")
        .where("name", ">=", prefix)
        .where("name", "<=", prefix + "\uf8ff")
        .stream()
    )
    return [u.to_dict() for u in users]


