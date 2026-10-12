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
    data = get_all_data()

    # 숫자로 변환할 수 있는 종가만 사용
    valid_data = []

    for item in data:
        try:
            price = float(item["value"])
            valid_data.append({**item, "value": price})
        except (KeyError, TypeError, ValueError):
            continue

    if not valid_data:
        return {
            "count": 0,
            "metrics": {},
            "trend": "분석할 데이터가 없습니다."
        }

    prices = [item["value"] for item in valid_data]

    # 최신 데이터부터 정렬되어 있으므로 최근 7개와
    # 그 이전 7개의 평균을 비교합니다.
    recent = prices[:7]
    previous = prices[7:14]

    if len(previous) < 7:
        trend = "비교 데이터 부족"
    else:
        recent_avg = sum(recent) / len(recent)
        previous_avg = sum(previous) / len(previous)

        if recent_avg > previous_avg:
            trend = "최근 7개 데이터 평균이 이전 7개보다 상승"
        elif recent_avg < previous_avg:
            trend = "최근 7개 데이터 평균이 이전 7개보다 하락"
        else:
            trend = "최근 7개 데이터 평균에 변화 없음"

    return {
        "count": len(valid_data),
        "metrics": {
            "average": round(sum(prices) / len(prices), 2),
            "max": round(max(prices), 2),
            "min": round(min(prices), 2)
        },
        "trend": trend
    }