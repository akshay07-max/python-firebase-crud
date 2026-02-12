import firebase_admin
from firebase_admin import auth, credentials, firestore

cred = credentials.Certificate("/firebase/python-firebase-crud-fc35d-firebase-adminsdk-fbsvc-6e33047372.json")

firebase_admin.initialize_app(cred)

db = firestore.client()