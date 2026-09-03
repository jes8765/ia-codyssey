from firebase.client import db

def get_all_conversations():
    docs = db.collection("conversations").order_by("timestamp").stream()
    result = []
    for doc in docs:
        data = doc.to_dict()
        result.append({
            "id": doc.id,
            **data
        })
    # 최신 대화가 위로 오도록 정렬
    result.reverse()
    return result