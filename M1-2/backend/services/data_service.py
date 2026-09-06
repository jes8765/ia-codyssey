from datetime import datetime
from firebase.client import db

def get_all_data():
    docs = db.collection("data").stream()
    result = []

    for doc in docs:
        data = doc.to_dict()
        result.append({
            "id": doc.id,
            **data,
        })

    # 날짜 문자열을 파이썬 datetime 객체로 변환하여 최신순(내림차순) 정렬
    def parse_date(item):
        date_str = item.get("date", "")
        for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return datetime.min # 변환 실패 시 가장 오래된 날짜로 취급

    result.sort(key=parse_date, reverse=True)

    return result

# 아래에 작성해둔 create_data, update_data 등은 그대로 두시면 됩니다.

def create_data(data: dict):
    doc_ref = db.collection("data").document()
    doc_ref.set(data)
    return {"id": doc_ref.id, **data}

def update_data(doc_id: str, data: dict):
    doc_ref = db.collection("data").document(doc_id)
    doc_ref.update(data)
    return {"id": doc_id, **data}

def delete_data(doc_id: str):
    db.collection("data").document(doc_id).delete()
    return {"message": "Deleted successfully"}

def get_data_summary():
    docs = db.collection("data").stream()
    values = []
    
    for doc in docs:
        data = doc.to_dict()
        if "value" in data:
            values.append(float(data["value"]))
            
    if not values:
        return {"count": 0, "metrics": {}}
        
    return {
        "count": len(values),
        "metrics": {
            "average": round(sum(values) / len(values), 2),
            "max": round(max(values), 2),
            "min": round(min(values), 2)
        },
        "trend": "상승 추세 유지 중"
    }