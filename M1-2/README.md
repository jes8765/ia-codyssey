# 📊 StockMate (NVDA AI Assistant) - 최종 과제 보고서

> **엔비디아(NVDA) 시계열 주가 데이터를 기반으로 통계적 요약 정보를 산출하고, 이를 OpenAI 시스템 프롬프트에 동적으로 컨텍스트 주입하여 개인화된 맞춤형 답변을 제공하는 Full-Stack AI 웹 서비스**

---

# 1. 프로젝트 개요

## 1.1 프로젝트 목적
일반적인 생성형 AI 서비스(ChatGPT 등)는 사용자가 보유한 구체적인 비즈니스 데이터나 개인화된 시계열 기록(예: 주가, 가계부 등)을 사전에 인지하지 못합니다. "현재 내 주가 상황이나 데이터 통계가 어때?"라고 물어도 일반적인 답변만 돌아오는 한계가 있습니다.

본 프로젝트는 이러한 한계를 극복하기 위해 **FastAPI 백엔드**, **Firebase Firestore**, 그리고 **OpenAI API**를 연동하여 사용자의 실제 시계열 데이터를 백그라운드에서 분석·요약하고, 이를 AI 대화의 컨텍스트로 실시간 주입하는 **'내 상황을 아는 AI 비서'**를 구축하는 것을 목표로 합니다.

또한 단순한 AI 대화에 그치지 않고 데이터 관리(CRUD), 요약 통계 산출, 대화 기록 저장 및 불러오기(History) 기능을 모두 포함한 완성도 있는 싱글 페이지 애플리케이션(SPA) 웹 서비스를 구현하고자 하였습니다.

---

## 1.2 프로젝트 배경
생성형 AI와 자동화 기술이 발전함에 따라 다양한 데이터 분석 도구가 등장하고 있지만, 개인이 보유한 시계열 데이터를 직접 AI와 연동하여 대화형으로 분석하는 서비스는 여전히 구현이 까다롭습니다. 

주가 데이터 분석 업무는 다음과 같은 한계와 요구사항을 지닙니다.
- 방대한 시계열 데이터(1,000건 이상)를 효율적으로 저장하고 관리해야 함
- AI가 사용자의 특정 데이터를 인지할 수 있도록 컨텍스트 주입 메커니즘이 필요함
- 사용자가 언제든지 데이터를 추가, 수정, 삭제할 수 있는 직관적인 CRUD 인터페이스 제공
- 과거 대화 내역을 보존하고 다시 확인할 수 있는 세션 관리 기능 필요

본 프로젝트에서는 **FastAPI + Firestore + OpenAI + Vanilla JS(SPA)** 구조를 설계하여, 사용자가 별도의 복잡한 설정 없이도 자신의 주가 데이터를 관리하고 AI를 통해 정밀한 분석을 받을 수 있는 환경을 구현하였습니다.

---

## 1.3 사용 기술

본 프로젝트에서 사용한 기술 스택은 다음과 같습니다.

| 기술 | 사용 목적 |
|------|-----------|
| **Python / FastAPI** | 고성능 백엔드 API 서버 구축 및 비동기 처리 |
| **Pydantic v2** | 엄격한 요청/응답 데이터 모델 검증 및 직렬화 |
| **Firebase Admin SDK / Firestore** | NoSQL 기반 시계열 주가 데이터 및 대화 기록 영구 저장 |
| **OpenAI API (`gpt-4o-mini`)** | 데이터 요약 컨텍스트가 주입된 맞춤형 AI 응답 생성 |
| **Vanilla HTML5 / CSS3 / JS** | 외부 프레임워크 없는 모던한 SPA 인터페이스 및 동적 DOM 제어 |
| **Render / Vercel** | 백엔드 및 프론트엔드 클라우드 배포 |

각 기술을 선택한 이유는 다음과 같습니다.

### FastAPI
FastAPI는 빠른 속도와 Pydantic을 이용한 자동 데이터 검증 기능 덕분에 AI 연동 백엔드를 구축하기에 매우 적합합니다. 비동기 처리를 지원하므로 대용량 데이터 조회 및 외부 OpenAI API 호출 시 병목 현상을 최소화할 수 있습니다.

### Firebase Firestore
NoSQL 기반의 Firestore는 문서(Document) 단위로 유연하게 데이터를 저장할 수 있어 시계열 주가 데이터와 구조화된 대화 세션 로그를 관리하는 데 최적화되어 있습니다. 서버리스 환경에서 쉽게 연동할 수 있는 장점이 있습니다.

### OpenAI API
`gpt-4o-mini` 모델은 뛰어난 자연어 이해 능력을 제공하면서도 비용 효율적입니다. 시스템 프롬프트(System Prompt)를 통해 실시간 연산된 주가 통계 요약을 주입함으로써 환각 현상을 줄이고 정확한 데이터 기반 답변을 유도할 수 있습니다.

### Vanilla JavaScript (SPA)
추가적인 프레임워크 설정 없이 브라우저 환경에서 가볍고 빠르게 동작하는 싱글 페이지 애플리케이션(SPA) 구조를 구현하여, 화면 깜빡임 없는 매끄러운 탭 전환과 직관적인 UI/UX를 제공합니다.

---

# 2. 시스템 구성

## 2.1 전체 워크플로우
본 프로젝트에서 구현한 전체 데이터 흐름 및 아키텍처는 다음과 같습니다.

```text
[Frontend (SPA)]
      │
      ├─ GET /api/data/summary ────────► [FastAPI Backend] ──(Firestore)──► 통계 요약 산출
      ├─ GET/POST/PUT/DEL /api/data ───► [FastAPI Backend] ──(Firestore)──► CRUD 처리
      ├─ POST /api/chat ───────────────► [FastAPI Backend] ──(OpenAI)────► 컨텍스트 주입 답변 생성 및 저장
      └─ GET /api/conversations ───────► [FastAPI Backend] ──(Firestore)──► 대화 기록 조회
```

---

## 2.2 핵심 모듈 및 API 설명

### Data API 및 Summary API
* **CRUD (`/api/data`)**: 1,254개의 NVDA 주가 데이터 포인트를 조회, 추가, 수정, 삭제할 수 있는 엔드포인트입니다.
* **Summary (`/api/data/summary`)**: 전체 데이터의 총 레코드 수, 평균가, 최고가, 최저가를 실시간으로 연산하여 반환합니다.

### Chat & Conversation API
* **Chat (`/api/chat`)**: 사용자의 질문을 받아 백그라운드에서 데이터 요약본을 결합한 시스템 프롬프트를 생성하고, OpenAI API를 호출한 뒤 대화 내용을 Firestore `conversations` 컬렉션에 자동 저장합니다.
* **Conversations (`/api/conversations`)**: 과거에 나눈 대화 세션 목록을 최신순으로 조회합니다.

---

# 3. 핵심 기능 및 아키텍처 구현

## 3.1 컨텍스트 주입 (Context Injection) 메커니즘
일반적인 LLM은 개인이 보유한 주가 데이터를 알지 못합니다. StockMate는 AI가 응답을 생성하기 전, 백엔드 서비스에서 `get_data_summary()`를 호출해 Firestore의 전체 주가 통계를 먼저 계산합니다.

이후 해당 통계 지표를 OpenAI API 호출 시 `system` 역할의 프롬프트에 동적으로 삽입합니다.

이 방식을 통해 AI는 사용자의 실제 데이터 범위 내에서 정확한 수치를 인용하여 답변할 수 있습니다.

## 3.2 싱글 페이지 애플리케이션 (SPA) UI
* **Overview 탭**: NVDA 주요 지표 및 AI 인사이트 카드 대시보드
* **Data 탭**: 아코디언 형태의 상세 주가 리스트 및 모달 기반 데이터 추가/삭제 인터페이스
* **AI Chat 탭**:실시간 메시지 버블, 로딩 애니메이션, 컨텍스트 기반 챗봇 인터페이스
* **History 탭**: 타임스탬프와 메시지 카운트가 표시되는 과거 대화 세션 아코디언 뷰

---

# 4. 프로젝트 디렉토리 구조

```text
ia-codyssey/M1-2/
├── backend/
│   ├── main.py                # FastAPI 앱 초기화 및 CORS 설정
│   ├── firebase/
│   │   └── client.py          # Firebase Firestore 초기화 설정
│   ├── schemas/
│   │   └── data.py            # Pydantic 데이터 검증 모델
│   ├── routers/
│   │   ├── data.py            # 데이터 CRUD 및 Summary 라우터
│   │   └── chat.py            # AI 챗봇 및 대화 기록 조회 라우터
│   └── services/
│       ├── data_service.py    # 데이터베이스 연동 및 통계 요약 로직
│       ├── openai_service.py  # OpenAI 프롬프트 주입 및 자동 저장 로직
│       └── conversation_service.py # 대화 기록 조회 로직
├── frontend/
│   ├── index.html             # SPA 메인 레이아웃 및 탭 구조
│   ├── style.css              # 다크 테마 및 네온 그린(#C8FF00) 스타일링
│   └── app.js                 # 화면 전환, 비동기 API 통신, 아코디언/모달 로직
├── .env.example               # 환경 변수 템플릿
└── README.md                  # 최종 프로젝트 보고서
```

---

# 5. 로컬 실행 및 설치 가이드

## 5.1 백엔드 실행 방법
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 5.2 프론트엔드 실행 방법
새로운 터미널 창에서 아래 명령어를 실행합니다.
```bash
cd frontend
python -m http.server 3000
# 브라우저에서 http://localhost:3000 접속
```

---

# 6. 환경 변수 설정
`backend/` 폴더 내에 `.env` 파일을 생성하고 아래 내용을 설정합니다.
```env
OPENAI_API_KEY=your_openai_api_key_here
FIREBASE_SERVICE_ACCOUNT_JSON=path_to_firebase_key.json
ALLOWED_ORIGINS=*
```

---

# 7. 배포 가이드
* **Backend (Render)**: GitHub 연동 후 Web Service 생성. 빌드 명령어 `pip install -r requirements.txt`, 실행 명령어 `uvicorn main:app --host 0.0.0.0 --port $PORT` 입력 및 환경 변수 등록.
* **Frontend (Vercel)**: 프론트엔드 폴더를 Vercel에 임포트하고, API 엔드포인트 주소를 배포된 Render 백엔드 URL로 연동.

---

# 결론
본 프로젝트는 FastAPI와 Firebase Firestore, OpenAI API를 결합하여 사용자의 시계열 데이터를 실시간으로 요약하고 대화의 컨텍스트로 주입하는 **StockMate** 웹 서비스를 성공적으로 구현하였다. 

데이터 관리(CRUD), 통계 요약, 맞춤형 AI 챗봇, 대화 기록 관리 기능을 순수 바닐라 웹 기술과 모던한 다크 테마 SPA 디자인으로 완성함으로써, 실제 개인화된 AI 비서 서비스가 동작하는 전체 아키텍처를 완벽하게 검증할 수 있었다.
