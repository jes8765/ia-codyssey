
import os
from datetime import datetime

from openai import OpenAI
from firebase.client import db
from services.data_service import get_all_data, get_data_summary

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def chat_with_ai(
    user_message: str,
    conversation_id: str | None = None,
):
    # 실제 Firestore 데이터 조회
    all_data = get_all_data()
    summary = get_data_summary()

    # 최근 20개 기록
    recent_data = [
        {
            "date": item.get("date"),
            "close": item.get("value"),
            "volume": item.get("volume"),
            "open": item.get("open"),
            "high": item.get("high"),
            "low": item.get("low"),
        }
        for item in all_data[:20]
    ]

    system_prompt = f"""
당신은 StockMate의 NVDA 주가 데이터 분석 비서입니다.
반드시 제공된 데이터에 근거해 한국어로 답변하세요.

[전체 데이터 요약]
- 유효 데이터 개수: {summary.get("count", 0)}
- 평균 종가: {summary.get("metrics", {}).get("average", "정보 없음")}
- 최고 종가: {summary.get("metrics", {}).get("max", "정보 없음")}
- 최저 종가: {summary.get("metrics", {}).get("min", "정보 없음")}
- 최근 추세: {summary.get("trend", "정보 없음")}

[최근 주가 기록: 최신순]
{recent_data}

[답변 규칙]
1. 가격과 거래량은 제공된 데이터에 근거하세요.
2. 제공되지 않은 날짜의 가격을 추측하지 마세요.
3. 데이터가 부족하면 부족하다고 알려주세요.
4. 과거 분석과 미래 예측을 구분하세요.
5. 투자 판단을 확정적으로 표현하지 마세요.
6. 상승 또는 하락을 설명할 때 비교 기준과 수치를 제시하세요.
"""

    conversations = db.collection("conversations")
    messages = []
    doc_ref = None

    # 기존 대화가 지정되었다면 이전 메시지를 불러옵니다.
    if conversation_id:
        doc_ref = conversations.document(conversation_id)
        snapshot = doc_ref.get()

        if not snapshot.exists:
            from fastapi import HTTPException
            raise HTTPException(
                status_code=404,
                detail="이어갈 대화 기록을 찾을 수 없습니다.",
            )

        saved_data = snapshot.to_dict() or {}
        messages = saved_data.get("messages", [])

    # 현재 질문 추가
    messages.append({
        "role": "user",
        "content": user_message,
    })

    # API에 보낼 역할과 내용만 사용
    api_messages = [{"role": "system", "content": system_prompt}]
    api_messages.extend(
        {
            "role": message["role"],
            "content": message["content"],
        }
        for message in messages
        if message.get("role") in ("user", "assistant")
        and isinstance(message.get("content"), str)
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=api_messages,
        temperature=0.3,
    )

    ai_reply = response.choices[0].message.content or ""

    messages.append({
        "role": "assistant",
        "content": ai_reply,
    })

    now = datetime.now().isoformat()

    conversation_data = {
        "timestamp": now,
        "messages": messages,
    }

    # 기존 대화라면 갱신, 새 대화라면 새 문서 생성
    if doc_ref is None:
        doc_ref = conversations.document()
        doc_ref.set(conversation_data)
    else:
        doc_ref.set(conversation_data)

    return {
        "reply": ai_reply,
        "conversation_id": doc_ref.id,
    }
