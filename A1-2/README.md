# 국내 여행 추천 프로그램

LLM(OpenAI API)과 Kakao Local API를 연동하여 여행 날짜에 맞는 국내 여행지를 추천하고, 맛집 정보를 검색하여 Markdown 여행 리포트를 생성하는 CLI 프로그램입니다.

---

# 목차

- [1. 프로젝트 소개](#1-프로젝트-소개)
- [2. 개발 환경](#2-개발-환경)
- [3. 프로젝트 구조](#3-프로젝트-구조)
- [4. 프로그램 동작 과정](#4-프로그램-동작-과정)
- [5. 기능 구현 과정](#5-기능-구현-과정)
- [6. 실행 방법](#6-실행-방법)
- [7. 실행 결과](#7-실행-결과)
- [8. 과제 요구사항 충족 여부](#8-과제-요구사항-충족-여부)
- [9. 배운 점](#9-배운-점)

---

# 1. 프로젝트 소개

## 프로젝트 개요

사용자가 여행 날짜를 입력하면 OpenAI API를 이용하여 국내 여행지를 추천하고, Kakao Local API를 통해 해당 지역의 맛집 정보를 검색합니다.

이후 추천 결과를 JSON 파일로 저장하고, Markdown 형식의 여행 리포트를 자동 생성합니다.

## 개발 목적

- OpenAI API 활용
- Kakao Local API 활용
- 여러 API를 하나의 서비스로 연동
- JSON 데이터 처리 학습
- Markdown 문서 자동 생성
- 예외 처리 및 API Key 관리 학습

## 주요 기능

- CLI 입력
- 날짜 검증
- 국내 여행지 추천
- 맛집 검색
- JSON 저장
- Markdown 리포트 생성
- 예외 처리
- API Key 관리

---

# 2. 개발 환경

## Language

- Python 3.12

## Library

- argparse
- requests
- openai
- python-dotenv
- json

## API

- OpenAI API (GPT-5-mini)
- Kakao Local API

---

# 3. 프로젝트 구조

```text
A1-2/
│
├── Travel_Plan.py
├── README.md
├── requirements.txt
├── .env
└── results/
    ├── YYYY-MM-DD_travel_info.json
    └── YYYY-MM-DD_travel_report.md
```

---

# 4. 프로그램 동작 과정

```text
사용자

↓

여행 날짜 입력

↓

OpenAI API

↓

추천 여행지(JSON)

↓

Kakao Local API

↓

맛집 검색

↓

travel_info.json 저장

↓

OpenAI API

↓

travel_report.md 생성
```

### 4.1 여행지 추천

사용자가 입력한 날짜를 기반으로 OpenAI API에서 국내 여행지를 추천받습니다.

### 4.2 맛집 검색

추천된 도시명을 Kakao Local API에 전달하여 맛집 정보를 검색합니다.

### 4.3 JSON 저장

추천 결과와 맛집 정보를 하나의 JSON 파일로 저장합니다.

### 4.4 Markdown 생성

추천 정보를 기반으로 Markdown 여행 리포트를 생성합니다.

---

# 5. 기능 구현 과정

## CLI 구현

`argparse`를 이용하여 여행 날짜를 입력받도록 구현했습니다.

```bash
python Travel_Plan.py --date "2026-07-25"
```

## 날짜 검증

`datetime.strptime()`를 이용하여 입력 형식을 검증했습니다.

## OpenAI API 연동

Responses API를 사용하여 JSON 형식의 여행 정보를 생성했습니다.

## Kakao Local API 연동

추천 도시명을 이용해 맛집 정보를 검색했습니다.

## JSON 구조화

OpenAI 응답을 `json.loads()`로 변환하여 프로그램에서 활용했습니다.

## Markdown 생성

추천 결과와 맛집 정보를 바탕으로 Markdown 리포트를 생성했습니다.

## 예외 처리

다음 상황을 처리하도록 구현했습니다.

- API 호출 실패
- JSON 파싱 실패
- 파일 저장 실패
- API Key 누락
- 맛집 검색 실패

---

# 6. 실행 방법

## 라이브러리 설치

```bash
pip install -r requirements.txt
```

## .env 설정

```env
OPENAI_API_KEY=YOUR_API_KEY
KAKAO_REST_API_KEY=YOUR_API_KEY
```

## 실행

```bash
python Travel_Plan.py --date "2026-07-25"
```

---


# 7. 과제 요구사항 충족 여부

| 요구사항 | 구현 |
|-----------|:---:|
| CLI 입력 | ✅ |
| 날짜 검증 | ✅ |
| OpenAI API | ✅ |
| Kakao Local API | ✅ |
| JSON 저장 | ✅ |
| Markdown 생성 | ✅ |
| 예외 처리 | ✅ |
| API Key 관리 | ✅ |

---

# 8. 배운 점

- LLM API와 외부 API를 연동하는 방법을 익혔습니다.
- JSON 데이터를 구조화하여 다른 API와 연계하는 방법을 학습했습니다.
- 예외 처리를 통해 프로그램의 안정성을 높이는 방법을 배웠습니다.
- `.env`를 이용하여 API Key를 안전하게 관리하는 방법을 익혔습니다.
