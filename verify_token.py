from firebase_admin import auth

# verify firebase token is used for api authentication.
def verify_token(id_token:str):
    decoded_token = auth.verify_id_token(id_token)
    return decoded_token