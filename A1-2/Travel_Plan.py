from dotenv import load_dotenv
from openai import OpenAI
import argparse
from datetime import datetime
import os
import json
import requests


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

대한민국 내 여행지만 추천하세요.
추천 도시는 반드시 한국의 도시 또는 지역만 가능합니다.

예시
- 서울
- 부산
- 강릉
- 제주
- 여수
- 경주

recommended_city에는 도시 이름만 작성하세요.

반드시 아래 JSON만 출력하세요.

{{
  "recommended_city":"",
  "weather":"",
  "events":[],
  "reason":""
  }}
"""
    
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        text = response.output_text

        try:
            travel_info = json.loads(text)
            return travel_info

        except json.JSONDecodeError:

            print("JSON 파싱 실패. 다시 요청합니다.")

            retry_prompt = prompt + """

        반드시 JSON만 출력하세요.
        설명은 절대 쓰지 마세요.
        """

            response = client.responses.create(
                model="gpt-5-mini",
                input=retry_prompt
            )

            travel_info = json.loads(response.output_text)

            return travel_info

    except Exception as e:
        print(f"❌ 여행 추천 생성 실패: {e}")
        return None
    

def search_restaurants(city):

    print("[2/3] 맛집 검색 중...")

    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    headers = {
        "Authorization": f"KakaoAK {os.getenv('KAKAO_REST_API_KEY')}"
    }

    params = {
        "query": f"{city} 맛집",
        "size": 5
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
    )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"❌ 맛집 검색 실패: {e}")
        return None
 

    data = response.json()

    restaurants = []

    for place in data["documents"]:
        restaurant = {
            "name": place["place_name"],
            "address": place["road_address_name"] if place["road_address_name"] else place["address_name"],
            "category": place["category_name"],
            "phone": place["phone"],
            "url": place["place_url"]
        }

        restaurants.append(restaurant)

    return restaurants

def save_travel_info(date, travel_info, restaurants, errors):

    data = {
    "recommended_city": travel_info["recommended_city"],
    "weather": travel_info["weather"],
    "events": travel_info["events"],
    "reason": travel_info["reason"],
    "restaurants": restaurants,
    "errors": errors
    }
       

    os.makedirs("results", exist_ok=True)

    try:
        with open(
            f"results/{date}_travel_info.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print("여행 정보 저장 완료!")

    except OSError as e:
        print(f"❌ 여행 정보 저장 실패: {e}")

def generate_report(client, date, travel_info, restaurants):

    print("[3/3] 최종 리포트 생성 중...")

    prompt = f"""
당신은 여행 플래너입니다.

아래 정보를 이용하여 Markdown 형식의 여행 리포트를 작성하세요.

# 여행 정보

도시 : {travel_info["recommended_city"]}

날씨 :
{travel_info["weather"]}

추천 이유 :
{travel_info["reason"]}

행사 :
{chr(10).join("- " + event for event in travel_info["events"])}

맛집 :

{chr(10).join(
    f"- {r['name']} ({r['category']})\n"
    f"  주소 : {r['address']}\n"
    f"  전화 : {r['phone']}\n"
    f"  링크 : {r['url']}"
    for r in restaurants
)}

Markdown만 출력하세요.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    report = response.output_text

    os.makedirs("results", exist_ok=True)

    with open(
        f"results/{date}_travel_report.md",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    print("리포트 저장 완료!")

    return report


def main():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
        print(".env 파일을 확인하세요.")
        return

    if not os.getenv("KAKAO_REST_API_KEY"):
        print("❌ KAKAO_REST_API_KEY가 설정되지 않았습니다.")
        print(".env 파일을 확인하세요.")
        return

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
    errors = []

    # 여행 추천
    travel_info = get_travel_recommendation(client, args.date)

    # ✅ 추가
    if travel_info is None:
        return

    # 맛집 검색
    restaurants = search_restaurants(
        travel_info["recommended_city"]
    )
    if restaurants is None:

        restaurants = []

        errors.append({
        "step":"place_search",
        "type":"API_ERROR",
        "message":"맛집 API 호출 실패"
        })

    elif not restaurants:

        print("⚠️ 맛집 정보를 가져오지 못했습니다.")

        errors.append({
        "step":"place_search",
        "type":"EMPTY_RESULT",
        "message":"검색 결과 없음"
        })

    save_travel_info(
        args.date,
        travel_info,
        restaurants,
        errors
    )

    report = generate_report(
        client,
        args.date,
        travel_info,
        restaurants
    )

    # ✅ 추가
    if report is None:
        return


if __name__ == "__main__":
    main()