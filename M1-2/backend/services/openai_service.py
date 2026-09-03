import os
from openai import OpenAI
from firebase.client import db
from datetime import datetime
from services.data_service import get_data_summary

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_with_ai(user_message: str):
    # 1. 데이터 요약 가져오기
    summary = get_data_summary()
    
    # 2. 시스템 프롬프트 구성 (컨텍스트 주입)
    system_prompt = f"""
    당신은 NVDA(엔비디아) 주가 데이터 분석 비서입니다.
    
    [사용자 데이터 요약]
    - 총 레코드: {summary.get('count', 0)}개
    - 주요 지표(평균/최고/최저): {summary.get('metrics', {})}
    - 최근 트렌드: {summary.get('trend', '분석 중')}
    
    위 데이터를 기반으로 사용자의 질문에 맞춤형 답변을 제공하세요.
    """
    
    # 3. OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    
    ai_reply = response.choices[0].message.content
    
    # 4. 대화 기록(Conversations) 자동 저장
    conversation_data = {
        "timestamp": datetime.now().isoformat(),
        "messages": [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": ai_reply}
        ]
    }
    db.collection("conversations").add(conversation_data)
    
    return {"reply": ai_reply}