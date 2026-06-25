# 프로젝트 3. RSS 기반 AI 뉴스 요약 자동화

## 프로젝트 목표

TechCrunch RSS에서 최신 기술 뉴스를 수집하고, AI 관련 기사만 선택하여 생성형 AI로 3줄 요약한 뒤 Notion 데이터베이스에 자동 저장하는 자동화 시스템을 구축한다.

---

# 개발 순서

## 1. 프로젝트 설계

### 목표

* [ ] 사용할 자동화 도구 선정 (Make)
* [ ] AI 모델 선정 (OpenAI GPT)
* [ ] 저장소 선정 (Notion)

---

## 2. RSS 선정

### RSS

```
https://techcrunch.com/feed/
```

### 확인 사항

* [ ] RSS 주소 정상 동작 확인
* [ ] 브라우저에서 XML 출력 확인
* [ ] RSS에서 가져오는 데이터 확인

  * 제목(Title)
  * 링크(Link)
  * 발행일(Published)
  * 본문(Description/Content)

---

## 3. Notion 데이터베이스 생성

데이터베이스 이름

```
AI News Summary
```

속성

| 속성        | 타입    |
| --------- | ----- |
| Title     | Title |
| Summary   | Text  |
| URL       | URL   |
| Published | Date  |

확인 사항

* [ ] 데이터베이스 생성
* [ ] Make 연동 준비

---

## 4. Make Scenario 생성

### 전체 구조

```
Scheduler
    ↓
RSS Feed
    ↓
Filter
    ↓
OpenAI
    ↓
Notion
```

---

## 5. Scheduler 설정

* [ ] 매일 09:00 실행
* [ ] Timezone : Asia/Seoul

---

## 6. RSS 연결

모듈

```
Retrieve RSS Feed Items
```

확인 사항

* [ ] RSS 연결 성공
* [ ] 기사 목록 출력 확인

---

## 7. 기사 필터링

필터 기준

```
AI
Artificial Intelligence
OpenAI
GPT
Gemini
Claude
LLM
Anthropic
Copilot
```

조건

* 제목 또는 본문에 키워드 포함

목표

* AI 관련 기사만 통과
* 최신 기사 1건 선택

---

## 8. OpenAI 연결

모듈

```
Create Chat Completion
```

프롬프트

```
다음 기술 뉴스를 한국어로 3줄 이내로 요약하세요.

제목
{{Title}}

본문
{{Description}}

조건
- 최대 3줄
- 핵심만 작성
- 한국어
```

확인 사항

* [ ] 요약 생성 성공

---

## 9. Notion 저장

모듈

```
Create Database Item
```

매핑

| Notion    | Make             |
| --------- | ---------------- |
| Title     | RSS Title        |
| Summary   | GPT Summary      |
| URL       | RSS Link         |
| Published | RSS Publish Date |

확인 사항

* [ ] Notion 저장 성공

---

## 10. 중복 저장 방지

방법

* URL 기준 검색
* 동일 URL 존재 시 저장하지 않음

구조

```
Search Database
        ↓
있음 → 종료

없음 → 저장
```

---

## 11. 오류 처리

RSS 실패

* 종료

OpenAI 실패

* 최대 2회 재시도

Notion 실패

* 최대 2회 재시도

---

## 12. 최종 테스트

### 테스트 목록

* [ ] RSS 수집
* [ ] 기사 필터링
* [ ] OpenAI 요약
* [ ] Notion 저장
* [ ] 중복 저장 확인
* [ ] Schedule 자동 실행 확인

---

# 최종 워크플로우

```
Scheduler
      ↓
RSS Feed
      ↓
AI 키워드 필터
      ↓
Notion 중복 검사(URL)
      ↓
없으면
      ↓
OpenAI 요약
      ↓
Notion 저장
```

---

# 프로젝트 완료 체크리스트

## 준비

* [ ] RSS 선정
* [ ] Notion DB 생성
* [ ] OpenAI API 준비
* [ ] Make Scenario 생성

## 기능

* [ ] RSS 수집
* [ ] AI 기사 필터링
* [ ] 기사 1건 선택
* [ ] AI 요약
* [ ] Notion 저장
* [ ] 중복 방지
* [ ] 오류 처리
* [ ] 자동 실행

## 결과물

* [ ] Make 워크플로우 캡처
* [ ] Notion 저장 화면 캡처
* [ ] README 작성
* [ ] 프로젝트 제출
