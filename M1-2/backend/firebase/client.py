import os
from firebase_admin import credentials, initialize_app, firestore

secret_file_path = "/etc/secrets/Firebase-key.json"
local_file_path = "./firebase-key.json"

if os.path.exists(secret_file_path):
    cred = credentials.Certificate(secret_file_path)
elif os.path.exists(local_file_path):
    cred = credentials.Certificate(local_file_path)
else:
    raise FileNotFoundError("Firebase key file not found.")

try:
    initialize_app(cred)
except ValueError:
    pass

db = firestore.client()