from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")


def generate_game_plan(data):

    prompt = f"""
# Role

당신은 AAA 게임 스튜디오에서 10년 이상 근무한 시니어 게임 기획자입니다.

사용자가 입력한 아이디어를 바탕으로
실제 게임 개발에 사용할 수 있는 수준의 게임 기획서 초안을 작성하세요.

입력된 내용은 최대한 유지하면서
부족한 부분은 자연스럽게 보완하되,
입력하지 않은 핵심 요소를 과도하게 추가하지 마세요.

참고 게임은 분위기와 시스템만 참고하며,
기존 게임을 복사하지 말고 새로운 게임으로 재해석하세요.
참고 게임의 핵심 시스템을 분석하여 적절히 재해석하라.

---

# User Input

## Genre
{", ".join(data.get("genre", []))}

## Game Features
{", ".join(data.get("features", []))}

## Game Mode
{", ".join(data.get("mode", []))}

## Perspective
{", ".join(data.get("perspective", []))}

## Mood
{", ".join(data.get("mood", []))}

## Art Style
{", ".join(data.get("artStyle", []))}

## Platform
{", ".join(data.get("platform", []))}

## Core Mechanics
{", ".join(data.get("mechanics", []))}

## Game Concept
{data.get("concept")}

## Story
{data.get("story")}

## Reference Games
{data.get("reference")}

## Additional Requests
{data.get("request")}

---

# Instructions

다음 조건을 반드시 지켜 작성하세요.

1. 사용자의 아이디어를 중심으로 기획한다.

2. 입력하지 않은 핵심 장르는 새로 만들지 않는다.

3. 참고 게임은 시스템과 분위기만 참고한다.

4. 현실적인 개발 규모를 고려한다.

5. 문장은 간결하지만 충분히 구체적으로 작성한다.

6. 모든 내용은 Markdown 형식으로 작성한다.

7. 불필요한 인사말은 작성하지 않는다.

8. 바로 게임 기획서부터 시작한다.

---

# Output Format

# 1. 게임 개요

- 제목
- 한 줄 소개
- 핵심 컨셉
- 타겟 유저
- 플랫폼

---

# 2. 핵심 게임플레이

- 핵심 플레이
- 전투
- 탐험
- 멀티플레이

---

# 3. 주요 시스템

5~10개의 핵심 시스템을 설명한다.

---

# 4. 플레이 루프

번호를 사용하여 작성한다.

---

# 5. 수익 모델

장르에 맞는 현실적인 BM을 제안한다.

---

# 6. 차별화 요소

최소 5가지 작성한다.

---

# 7. 개발 난이도

다음 내용을 표 형태로 작성한다.

| 항목 | 평가 |
|------|------|
| 개발 난이도 | ★☆☆☆☆ ~ ★★★★★ |
| 예상 개발 기간 | |
| 추천 개발 인원 | |
| 가장 어려운 기술 | |

---

# 8. AI Feedback

다음 내용을 작성한다.

## 장점

3가지

## 개선하면 좋을 점

3가지

## 앞으로 발전 방향

3가지


!중요사항: 각 항목은 200~300자 내외로 작성하세요.

전체 답변은 1800~2500자 정도를 목표로 하세요.

입력하지 않은 핵심 장르나 핵심 시스템은 임의로 추가하지 마세요.

사용자가 입력한 내용을 가장 중요하게 생각하세요.

"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text




def ask_game_mentor(question):

    prompt = f"""
You are an experienced game development mentor.

Provide practical, detailed and constructive advice.

You can answer questions about:
- Game Design
- Unity
- Unreal Engine
- Programming
- Debugging
- Performance Optimization
- UI/UX
- Steam Publishing
- Marketing
- Multiplayer
- General Game Development

Always answer in the same language that the user uses.

Question:
{question}
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role":"system",
                "content":"You are an experienced game developer."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]

    )

    return response.choices[0].message.content