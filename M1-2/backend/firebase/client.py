import json
import os

import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv


load_dotenv()

firebase_key_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")

if not firebase_key_path:
    raise ValueError("FIREBASE_SERVICE_ACCOUNT_JSON 환경변수가 설정되지 않았습니다.")

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_key_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()