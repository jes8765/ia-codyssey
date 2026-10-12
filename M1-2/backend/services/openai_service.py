
import os
from datetime import datetime

from openai import OpenAI
from firebase.client import db
from services.data_service import get_all_data, get_data_summary

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def chat_with_ai(user_message: str):
    # 실제 Firestore 데이터 조회
    all_data = get_all_data()
    summary = get_data_summary()

    # 최근 20개 데이터의 필요한 필드만 전달
    recent_data = []

    for item in all_data[:20]:
        recent_data.append({
            "date": item.get("date"),
            "close": item.get("value"),
            "volume": item.get("volume"),
            "open": item.get("open"),
            "high": item.get("high"),
            "low": item.get("low")
        })

    system_prompt = f"""
당신은 StockMate의 NVDA 주가 데이터 분석 비서입니다.

반드시 아래에 제공된 실제 데이터를 근거로 답변하세요.

[전체 데이터 요약]
- 유효 데이터 개수: {summary.get("count", 0)}
- 평균 종가: {summary.get("metrics", {}).get("average", "정보 없음")}
- 최고 종가: {summary.get("metrics", {}).get("max", "정보 없음")}
- 최저 종가: {summary.get("metrics", {}).get("min", "정보 없음")}
- 최근 추세: {summary.get("trend", "정보 없음")}

[최근 주가 기록: 최신순]
{recent_data}

[답변 규칙]
1. 한국어로 답변하세요.
2. 가격과 거래량은 제공된 데이터에 근거하세요.
3. 최근 기록에 없는 특정 날짜의 가격은 추측하지 마세요.
4. 필요한 데이터가 제공되지 않았다면 데이터가 부족하다고 알려주세요.
5. 과거 데이터 분석과 미래 예측을 구분하세요.
6. 투자 판단은 확정적으로 표현하지 마세요.
7. 상승 또는 하락이라고 설명할 때는 가능한 한 비교 기준과 수치를 제시하세요.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3
    )

    ai_reply = response.choices[0].message.content

    # 사용자 질문과 AI 답변 저장
    conversation_data = {
        "timestamp": datetime.now().isoformat(),
        "messages": [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": ai_reply}
        ]
    }

    db.collection("conversations").add(conversation_data)

    return {"reply": ai_reply}