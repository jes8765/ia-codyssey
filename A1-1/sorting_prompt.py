# ===============================
# Prompt Manager v1
# 프로젝트 구조 설계
# ===============================


# ---------------- Prompt 클래스 ----------------
class Prompt:

    def __init__(self, title, content, category, favorite=False):
        self.title = title
        self.content = content
        self.category = category
        self.favorite = favorite

    def print_list(self):
        star = "⭐" if self.favorite else ""
        print(f"[{self.category}] {self.title} {star}")

    def print_detail(self):
        print("-" * 40)
        print(f"제목 : {self.title}")
        print(f"카테고리 : {self.category}")
        print(f"즐겨찾기 : {'⭐' if self.favorite else '없음'}")
        print("-" * 40)
        print(self.content)
        print("-" * 40)


# ---------------- Prompt 관리 클래스 ----------------
class PromptManager:

    def __init__(self):

        self.prompts = [

            Prompt(
                "레고 광고 이미지 생성",
                "레고 스타일의 우주 고래 광고 이미지를 생성해주세요.",
                "이미지 생성",
                True
            ),

            Prompt(
                "게임 기획 도우미",
                "당신은 10년 경력의 게임 기획자입니다. 아이디어를 발전시켜 주세요.",
                "텍스트 생성"
            ),

            Prompt(
                "AI 뉴스 자동화",
                "AI 관련 최신 뉴스를 3줄로 요약해주세요.",
                "자동화"
            )

        ]

    # 프롬프트 추가
    def add_prompt(self):
        pass

    # 프롬프트 목록
    def show_prompt_list(self):
        pass

    # 카테고리 조회
    def show_by_category(self):
        pass

    # 검색
    def search_prompt(self):
        pass

    # 상세 보기
    def show_prompt_detail(self):
        pass

    # 즐겨찾기 추가/해제
    def toggle_favorite(self):
        pass

    # 즐겨찾기 목록
    def show_favorites(self):
        pass


# ---------------- 메인 앱 ----------------
# ---------------- 메인 앱 ----------------
class PromptApp:

    def __init__(self):
        self.manager = PromptManager()

    # 메뉴 출력
    def print_menu(self):

        print("\n===== Prompt Manager =====")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록")
        print("3. 카테고리 조회")
        print("4. 프롬프트 검색")
        print("5. 프롬프트 상세 보기")
        print("6. 즐겨찾기 관리")
        print("7. 즐겨찾기 목록")
        print("0. 종료")

    # 프로그램 실행
    def run(self):

        while True:

            self.print_menu()

            choice = input("선택 : ")

            if choice == "1":
                print("프롬프트 추가 기능 구현 예정")

            elif choice == "2":
                print("프롬프트 목록 기능 구현 예정")

            elif choice == "3":
                print("카테고리 조회 기능 구현 예정")

            elif choice == "4":
                print("검색 기능 구현 예정")

            elif choice == "5":
                print("상세 보기 기능 구현 예정")

            elif choice == "6":
                print("즐겨찾기 관리 기능 구현 예정")

            elif choice == "7":
                print("즐겨찾기 목록 기능 구현 예정")

            elif choice == "0":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다.")


# ---------------- 프로그램 시작 ----------------
app = PromptApp()
app.run()