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


def delete_conversation(conversation_id: str):
    doc_ref = db.collection("conversations").document(conversation_id)

    # 없는 문서를 삭제 성공으로 처리하지 않도록 확인
    if not doc_ref.get().exists:
        return False

    doc_ref.delete()
    return True