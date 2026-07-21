from dotenv import load_dotenv
from openai import OpenAI
import argparse
from datetime import datetime
import os
import json


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError(
            "날짜는 YYYY-MM-DD 형식이어야 합니다."
        )


def get_travel_recommendation(client, date):

    print("[1/3] 여행 추천 생성 중...")

    prompt = f"""
사용자가 여행을 가는 날짜는 {date}입니다.

반드시 아래 JSON만 출력하세요.
recommended_city는 대한민국을 제외한 도시명만 작성하세요.
예: 제주, 강릉, 부산
설명은 절대 하지 마세요.

{{
  "recommended_city": "",
  "weather": "",
  "events": [],
  "reason": ""
}}
"""
    
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    text = response.output_text

    print(text)

    travel_info = json.loads(text)

    return travel_info


def search_restaurants(city):
    print("[2/3] 맛집 검색 중...")


def generate_report():
    print("[3/3] 최종 리포트 생성 중...")


def main():
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    parser = argparse.ArgumentParser(
        description="국내 여행 추천 프로그램"
    )

    parser.add_argument(
        "--date",
        required=True,
        type=validate_date,
        help="여행 날짜 (YYYY-MM-DD)"
    )

    args = parser.parse_args()

    print(f"입력한 여행 날짜: {args.date}")

    travel_info = get_travel_recommendation(client, args.date)
    print(travel_info)

    search_restaurants("")
    generate_report()


if __name__ == "__main__":
    main()