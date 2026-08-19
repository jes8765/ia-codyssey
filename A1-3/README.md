# GameForge AI

AI를 활용하여 게임 아이디어를 구체적인 게임 기획으로 발전시키고, 게임 개발 과정에서 필요한 조언을 받을 수 있는 AI 기반 게임 개발 지원 웹 서비스입니다.

사용자는 게임의 장르, 특징, 플레이 방식, 시점, 분위기, 아트 스타일 등의 정보를 입력하여 AI가 생성한 게임 기획서를 확인할 수 있으며, AI Mentor를 통해 게임 개발과 관련된 질문도 할 수 있습니다.

> **배포 URL:** https://ia-codyssey.onrender.com

---

## 1. 프로젝트 소개

### 1.1 프로젝트 개요

- **프로젝트명:** GameForge AI
- **프로젝트 형태:** AI 기반 게임 개발 지원 웹 서비스
- **Frontend:** HTML / CSS / JavaScript
- **Backend:** Python / Flask
- **AI:** OpenAI API
- **배포:** Render

### 1.2 기획 배경

게임 아이디어를 가지고 있어도 장르, 핵심 게임플레이, 주요 시스템, 플레이 방식 등 구체적인 기획 요소를 정리하는 과정에서 어려움을 겪을 수 있습니다.

GameForge AI는 이러한 과정을 AI가 보조하도록 하여 사용자의 게임 아이디어를 보다 구체적인 게임 기획으로 발전시키는 것을 목표로 제작했습니다.

### 1.3 서비스 목표

- 게임 아이디어를 구체적인 게임 기획으로 발전시키기
- 게임 기획에 필요한 요소를 체계적으로 정리하기
- 게임 개발 과정에서 필요한 질문에 AI를 활용해 답변받기
- 실제 사용자가 접속할 수 있는 AI 웹 서비스를 구현하기

### 1.4 타겟 사용자

- 게임 개발을 처음 시작하는 사용자
- 게임 아이디어를 구체화하고 싶은 사용자
- 인디 게임 개발자
- Unity 및 Unreal Engine 등 게임 개발을 공부하는 사용자

---

## 2. 주요 기능

### 2.1 AI Planner

사용자가 게임에 대한 정보를 입력하면 OpenAI API를 통해 게임 기획서를 생성합니다.

주요 입력 항목은 다음과 같습니다.

- Genre
- Game Features
- Game Mode
- Perspective
- Mood
- Art Style
- Platform
- Core Mechanics
- Game Concept
- Story
- Reference Games
- Additional Requests

생성 결과에는 다음과 같은 내용이 포함됩니다.

- 게임 개요
- 핵심 게임플레이
- 주요 시스템
- 플레이 루프
- 수익 모델
- 차별화 요소
- 개발 난이도
- AI Feedback

### 2.2 AI Mentor

게임 개발과 관련된 질문을 입력하면 AI가 답변합니다.

게임 기획, 프로그래밍, Unity, Unreal Engine, UI/UX, 디버깅, 최적화 등 게임 개발 과정에서 필요한 다양한 질문에 사용할 수 있습니다.

### 2.3 Resources

게임 개발에 참고할 수 있는 자료를 확인할 수 있는 페이지입니다.

### 2.4 반응형 웹

데스크톱과 모바일 환경에서 사용할 수 있도록 CSS Media Query를 활용하여 반응형 레이아웃을 적용했습니다.

---

## 3. 페이지 구성

### 3.1 Main

GameForge AI의 서비스와 주요 기능을 소개하는 메인 페이지입니다.

상단 네비게이션을 통해 각 기능으로 이동할 수 있습니다.

### 3.2 Planner

게임 정보를 입력하고 AI가 게임 기획서를 생성하는 페이지입니다.

### 3.3 Mentor

게임 개발과 관련된 질문을 입력하고 AI의 답변을 확인하는 페이지입니다.

### 3.4 Resources

게임 개발 관련 자료를 확인할 수 있는 페이지입니다.

### 3.5 네비게이션

```text
Main
 ├── Planner
 ├── Resources
 └── Mentor
```

---

## 4. AI 기능 동작 방식

### 4.1 전체 요청 흐름

```text
사용자 입력
    ↓
JavaScript
    ↓
fetch()
    ↓
Flask API
    ↓
OpenAI API
    ↓
AI 응답
    ↓
Flask JSON 응답
    ↓
JavaScript
    ↓
웹페이지에 결과 표시
```

### 4.2 Planner API

```text
POST /api/planner
```

사용자가 입력한 게임 기획 정보를 Flask 서버로 전달하고 OpenAI API를 호출하여 게임 기획 결과를 반환합니다.

### 4.3 Mentor API

```text
POST /api/mentor
```

사용자가 입력한 질문을 Flask 서버로 전달하고 OpenAI API를 호출하여 게임 개발 관련 답변을 반환합니다.

### 4.4 테스트 API

```text
GET /api/test
```

백엔드 서버가 정상적으로 동작하는지 확인하기 위한 테스트 API입니다.

### 4.5 입력 검증 및 오류 처리

Planner에서 요청 데이터가 없는 경우 요청을 거부하도록 구현했습니다.

```json
{
  "error": "Request data is required"
}
```

Mentor에서 질문이 입력되지 않은 경우 다음과 같이 처리합니다.

```json
{
  "error": "Question is required"
}
```

AI API 호출 과정에서 예외가 발생한 경우 서버에서 오류를 처리하고 실패 응답을 반환합니다.

---

## 5. 기술 스택

| 구분 | 기술 |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| AI | OpenAI API |
| WSGI Server | Gunicorn |
| Version Control | Git, GitHub |
| Deployment | Render |

프론트엔드는 React나 Vue 등의 프레임워크를 사용하지 않고 순수 HTML/CSS/JavaScript로 구현했습니다.

---

## 6. 프로젝트 구조

```text
A1-3/
├── api/
│   └── index.py
├── css/
├── js/
├── images/
├── data/
├── index.html
├── planner.html
├── mentor.html
├── resources.html
├── openai_service.py
├── requirements.txt
└── README.md
```

### 주요 파일

| 파일 | 역할 |
|---|---|
| `index.html` | 메인 페이지 |
| `planner.html` | AI Planner 페이지 |
| `mentor.html` | AI Mentor 페이지 |
| `resources.html` | Resources 페이지 |
| `api/index.py` | Flask API 서버 |
| `openai_service.py` | OpenAI API 호출 기능 |
| `css/` | 페이지 스타일 및 반응형 디자인 |
| `js/` | 사용자 입력, API 요청 및 결과 처리 |
| `images/` | 웹페이지 이미지 |
| `data/` | 서비스 데이터 |
| `requirements.txt` | Python 의존성 관리 |

---

## 7. 환경 변수

OpenAI API Key는 소스 코드에 직접 작성하지 않고 환경 변수로 관리합니다.

사용하는 환경 변수는 다음과 같습니다.

```text
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

`OPENAI_MODEL`이 설정되지 않은 경우 코드에서 `gpt-5-mini`를 기본 모델로 사용하도록 구성했습니다.

API Key는 GitHub 저장소에 포함하지 않으며 배포 환경에서도 환경 변수로 관리합니다.

---

## 8. 로컬 실행 방법

### 8.1 저장소 복제

```bash
git clone https://github.com/jes8765/ia-codyssey.git
cd ia-codyssey/A1-3
```

### 8.2 가상환경 생성

```bash
python3 -m venv .venv
```

### 8.3 가상환경 활성화

macOS / Linux:

```bash
source .venv/bin/activate
```

### 8.4 패키지 설치

```bash
pip install -r requirements.txt
```

### 8.5 환경 변수 설정

로컬 환경에서 OpenAI API Key를 환경 변수로 설정합니다.

```text
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

### 8.6 서버 실행

```bash
gunicorn api.index:app
```

---

## 9. 배포

### 9.1 배포 환경

GitHub 저장소를 기반으로 Render Web Service에 배포했습니다.

Render에서 `requirements.txt`에 정의된 Python 패키지를 설치하고 Gunicorn을 이용하여 Flask 애플리케이션을 실행합니다.

### 9.2 배포 URL

**GameForge AI**

https://ia-codyssey.onrender.com

### 9.3 배포 과정에서 발생한 문제

처음에는 과제의 요구사항에 따라 Vercel을 이용하여 Flask API를 배포하려고 했습니다.

그러나 Vercel에서 Flask API의 라우팅 과정에서 반복적으로 `404: NOT_FOUND`가 발생했습니다. `/api/test`와 같은 단순한 테스트 API에서도 404가 발생하여 라우팅 구조를 확인하는 과정을 거쳤습니다.

이후 Flask 서버를 직접 실행할 수 있는 Render Web Service 방식으로 배포 구조를 변경했습니다.

Render 배포 초기에는 다음과 같은 오류도 발생했습니다.

```text
gunicorn: command not found
```

이를 해결하기 위해 `requirements.txt`에 Gunicorn을 추가했습니다.

이후 Flask 서버 실행과 API 호출을 확인하고 정적 파일 제공 문제를 수정하여 최종 배포를 완료했습니다.

### 9.4 배포 후 확인

배포된 환경에서 다음 기능을 확인했습니다.

- 메인 페이지 접속
- Planner 페이지 이동
- Mentor 페이지 이동
- Resources 페이지 이동
- API 테스트
- AI Planner 응답
- AI Mentor 응답
- 모바일 화면

---

## 10. 반응형 웹

모바일 환경에서도 사용할 수 있도록 CSS Media Query를 적용했습니다.

모바일 환경에서는 다음 요소를 조정했습니다.

- 헤더 높이
- 로고 크기
- 네비게이션 간격
- Hero 영역 배치
- Hero 이미지 크기
- 버튼 크기
- 카드 배치
- 콘텐츠 여백

특히 메인 페이지의 데스크톱 2열 레이아웃을 모바일에서는 세로 방향으로 변경하여 작은 화면에서도 콘텐츠를 확인할 수 있도록 수정했습니다.

---

## 11. 개발 과정 및 문제 해결

### 11.1 AI 코딩 도구 활용

프로젝트의 HTML, CSS, JavaScript, Python 코드 작성과 기능 구현 과정에서 AI 코딩 도구를 활용했습니다.

AI가 생성한 코드를 그대로 사용하는 것에 그치지 않고 실제 실행 결과와 오류 메시지를 확인하면서 필요한 부분을 수정했습니다.

### 11.2 API 연동

JavaScript의 `fetch()`를 이용하여 프론트엔드에서 Flask 백엔드로 요청을 전달했습니다.

Flask는 요청 데이터를 확인한 후 OpenAI API를 호출하고 결과를 JSON 형태로 프론트엔드에 반환하도록 구성했습니다.

### 11.3 배포 문제 해결

배포 과정에서는 로컬 환경과 실제 서버 환경의 차이로 인해 여러 문제가 발생했습니다.

대표적으로 다음 문제를 경험했습니다.

- Vercel API 404 오류
- Flask 라우팅 문제
- Gunicorn 실행 문제
- 정적 HTML/CSS/이미지 제공 문제
- 배포 환경에서 AI API 호출 확인

각 문제를 로그와 실제 응답을 확인하면서 원인을 좁혀가고 수정했습니다.

### 11.4 문제 해결 과정

```text
문제 발생
   ↓
오류 메시지 확인
   ↓
현재 코드와 프로젝트 구조 확인
   ↓
원인 분석
   ↓
수정
   ↓
로컬 테스트
   ↓
배포
   ↓
실제 서비스에서 재확인
```

---

## 12. Git 관리

프로젝트는 GitHub를 이용하여 버전 관리했습니다.

기능을 구현할 때 변경 내용을 커밋하여 개발 과정과 변경 사항을 기록했으며, 기능 구현과 오류 수정 과정에서 여러 커밋을 남겼습니다.

주요 개발 흐름은 다음과 같습니다.

```text
프로젝트 초기 구성
        ↓
웹페이지 구현
        ↓
Planner 구현
        ↓
Mentor 구현
        ↓
OpenAI API 연동
        ↓
Backend API 통합
        ↓
배포 시도
        ↓
배포 오류 수정
        ↓
Render 배포
        ↓
반응형 수정
        ↓
최종 테스트
```

---

## 13. 테스트

### 13.1 Planner 정상 입력

게임 정보를 입력한 후 AI Planner를 실행하여 게임 기획서가 정상적으로 생성되는 것을 확인했습니다.

### 13.2 Mentor 정상 입력

게임 개발과 관련된 질문을 입력한 후 AI Mentor의 답변이 정상적으로 출력되는 것을 확인했습니다.

### 13.3 빈 입력

Planner와 Mentor에서 필수 입력값이 없는 경우 API에서 요청을 검증하고 오류 메시지를 반환하는 것을 확인했습니다.

### 13.4 모바일 테스트

모바일 환경에서 다음 요소를 확인했습니다.

- 메인 페이지
- 네비게이션
- Planner
- Mentor
- Resources
- AI 결과 화면

### 13.5 배포 테스트

최종 배포 URL에서 주요 페이지 이동과 AI 기능을 확인했습니다.

| 항목 | 결과 |
|---|---|
| Main | 정상 |
| Planner | 정상 |
| Mentor | 정상 |
| Resources | 정상 |
| API Test | 정상 |
| AI Planner | 정상 |
| AI Mentor | 정상 |
| 모바일 화면 | 정상 |

---

## 14. 프로젝트 결과

GameForge AI는 게임 아이디어를 입력하면 AI를 통해 게임 기획서를 생성하고, 게임 개발과 관련된 질문에도 답변을 받을 수 있는 웹 서비스로 구현되었습니다.

HTML/CSS/JavaScript 기반의 프론트엔드와 Python Flask 기반의 백엔드를 연결하고 OpenAI API를 연동했습니다.

또한 GitHub를 이용해 프로젝트를 관리하고 Render를 통해 실제 인터넷에서 접속할 수 있는 서비스로 배포했습니다.

---

## 15. 과제 요구사항 구현 결과

| 요구사항 | 구현 |
|---|---|
| 서비스 아이디어 정의 | 완료 |
| 목적 및 타겟 사용자 정의 | 완료 |
| 3개 이상 페이지 구성 | 완료 |
| HTML/CSS/JavaScript 구현 | 완료 |
| 페이지 네비게이션 | 완료 |
| 반응형 웹 | 완료 |
| AI 입력 UI | 완료 |
| AI 결과 출력 | 완료 |
| AI API 연동 | 완료 |
| Python 백엔드 | 완료 |
| 환경 변수 사용 | 완료 |
| GitHub 저장소 | 완료 |
| 실제 URL 배포 | 완료 |
| README 작성 | 완료 |
| 서비스 기획서 | 별도 작성 |
| 서비스 스크린샷 | 별도 준비 |
| AI 코딩 도구 사용 증빙 | 별도 준비 |

---

## 16. 향후 발전 방향

### 게임 기획서 저장

생성된 게임 기획서를 저장하고 이전에 생성한 기획서를 다시 확인할 수 있는 기능을 추가할 수 있습니다.

### 게임 기획서 수정

AI가 생성한 기획서의 특정 부분만 선택하여 다시 수정하거나 발전시킬 수 있는 기능을 추가할 수 있습니다.

### 프로젝트 관리

게임 기획뿐만 아니라 개발 일정, 작업 목록, 개발 단계 등을 관리할 수 있는 기능으로 확장할 수 있습니다.

### AI 개발 지원 확대

Unity 및 Unreal Engine 코드 작성, 디버깅, 최적화 등 실제 게임 개발 과정에서 사용할 수 있는 AI 기능을 추가할 수 있습니다.

---

## 17. 느낀 점 및 배운 점

이번 프로젝트를 통해 AI를 활용하여 코드를 작성하는 것과 실제로 하나의 웹 서비스를 완성하는 것은 다른 문제라는 것을 경험했습니다.

AI를 활용하면 HTML, CSS, JavaScript, Python 등의 코드를 빠르게 작성할 수 있었지만 실제 개발 과정에서는 프론트엔드와 백엔드의 연결, API 경로, 환경 변수, 파일 구조, 배포 환경 등 여러 요소를 함께 이해해야 했습니다.

특히 로컬 환경에서는 정상적으로 동작하던 코드가 배포 환경에서 404 오류를 발생시키거나 정적 파일이 제대로 표시되지 않는 문제를 직접 해결하면서 배포 환경과 로컬 환경의 차이를 이해할 수 있었습니다.

또한 AI가 생성한 코드에 문제가 발생했을 때 새로운 코드를 무작정 생성하는 것보다 오류 로그와 현재 프로젝트 구조를 확인하고 원인을 파악한 뒤 수정하는 과정이 중요하다는 것을 배웠습니다.

이번 경험을 통해 AI를 단순한 코드 생성 도구가 아니라 개발 과정에서 구현 속도를 높이고 문제 해결을 보조하는 도구로 활용할 수 있다는 것을 배웠습니다.
