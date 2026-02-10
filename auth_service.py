from firebase_admin import auth # firebase admin provides auth library for authentication

def create_user(email: str, password: str, name: str):
    user = auth.create_user(
        email=email,
        password = password,
        display_name = name
    )

    return user.uid

def get_user(uid:str):
    return auth.get_user(uid)

def delete_user(uid:str):
    return auth.delete_user(uid)

