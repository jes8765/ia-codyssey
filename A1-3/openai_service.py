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
당신은 전문 게임 기획자입니다.

아래 정보를 참고하여 게임 기획서를 작성하세요.

장르:
{data.get("genre")}

게임 특징:
{data.get("features")}

게임 모드:
{data.get("mode")}

시점:
{data.get("perspective")}

분위기:
{data.get("mood")}

아트 스타일:
{data.get("artStyle")}

플랫폼:
{data.get("platform")}

핵심 메커니즘:
{data.get("mechanics")}

게임 컨셉:
{data.get("concept")}

스토리:
{data.get("story")}

참고 게임:
{data.get("reference")}

추가 요청:
{data.get("request")}

위 정보를 기반으로
1. 게임 개요
2. 핵심 게임플레이
3. 주요 시스템
4. 플레이 루프
5. 수익 모델
6. 차별화 요소
를 Markdown 형식으로 작성하세요.
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text