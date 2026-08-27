from firebase.client import db


test_ref = db.collection("data").document("connection-test")

test_ref.set({
    "message": "Firebase connection successful"
})

print("Firebase 연결 성공!")