import json
import os
from pathlib import Path

from firebase_admin import credentials, initialize_app, firestore

secret_file_path = "/etc/secrets/Firebase-key.json"
local_file_path = Path(__file__).resolve().parent.parent / "firebase-key.json"

firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")

if firebase_json:
    cred = credentials.Certificate(json.loads(firebase_json))
elif os.path.exists(secret_file_path):
    cred = credentials.Certificate(secret_file_path)
elif local_file_path.exists():
    cred = credentials.Certificate(str(local_file_path))
else:
    raise FileNotFoundError("Firebase key file not found.")

try:
    initialize_app(cred)
except ValueError:
    pass

db = firestore.client()