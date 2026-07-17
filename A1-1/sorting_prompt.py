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

        print("\n===== 프롬프트 추가 =====")

        while True:
            title = input("제목 : ").strip()

            if title:
                break

            print("제목은 비워둘 수 없습니다.")

        while True:
            content = input("내용 : ").strip()

            if content:
                break
    
            print("내용은 비워둘 수 없습니다.")

        categories = [
            "텍스트 생성",
            "이미지 생성",
            "영상 생성",
            "페르소나",
            "자동화",
            "기타"
        ]

        print("\n카테고리")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = input("번호 선택 (직접 입력은 Enter) : ").strip()

        if choice.isdigit():

            index = int(choice) - 1

            if 0 <= index < len(categories):
                category = categories[index]
            else:
                category = input("카테고리 직접 입력 : ")

        else:

            category = input("카테고리 직접 입력 : ")

        new_prompt = Prompt(
            title,
            content,
            category
        )

        self.prompts.append(new_prompt)

        print("\n프롬프트가 추가되었습니다.")


    # 프롬프트 목록
    def show_prompt_list(self):

        print("\n===== 프롬프트 목록 =====")

        if not self.prompts:
            print("등록된 프롬프트가 없습니다.")
            return

        for i, prompt in enumerate(self.prompts, start=1):
            print(f"{i}. ", end="")
            prompt.print_list()

        print(f"\n총 {len(self.prompts)}개의 프롬프트")

    # 카테고리 조회
    def show_by_category(self):

        categories = [
            "텍스트 생성",
            "이미지 생성",
            "영상 생성",
            "페르소나",
            "자동화",
            "기타"
        ]

        print("\n===== 카테고리 조회 =====")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = input("번호 선택 : ")

        if not choice.isdigit():
            print("잘못된 입력입니다.")
            return

        index = int(choice) - 1
    
        if index < 0 or index >= len(categories):
            print("잘못된 입력입니다.")
            return

        selected = categories[index]

        print(f"\n===== {selected} =====")

        count = 0

        for prompt in self.prompts:
            if prompt.category == selected:
                count += 1
                print(f"{count}. ", end="")
                prompt.print_list()

        if count == 0:
            print("해당 카테고리의 프롬프트가 없습니다.")
        else:
            print(f"\n총 {count}개의 프롬프트")
    # 검색
    def search_prompt(self):

        keyword = input("\n검색어 입력 : ").strip()

        if keyword == "":
            print("검색어를 입력해주세요.")
            return

        print("\n===== 검색 결과 =====")

        count = 0

        for prompt in self.prompts:

            if keyword.lower() in prompt.title.lower() or \
               keyword.lower() in prompt.content.lower():

                count += 1
                print(f"{count}. ", end="")
                prompt.print_list()

        if count == 0:
            print("검색 결과가 없습니다.")
        else:
            print(f"\n총 {count}개의 검색 결과")

    # 상세 보기
    def show_prompt_detail(self):

        if not self.prompts:
            print("등록된 프롬프트가 없습니다.")
            return

        print("\n===== 프롬프트 목록 =====")

        for i, prompt in enumerate(self.prompts, start=1):
            print(f"{i}. ", end="")
            prompt.print_list()

        choice = input("\n번호 선택 : ")

        if not choice.isdigit():
            print("잘못된 입력입니다.")
            return

        index = int(choice) - 1

        if index < 0 or index >= len(self.prompts):
            print("잘못된 번호입니다.")
            return

        print("\n===== 프롬프트 상세 =====")
        self.prompts[index].print_detail()

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
                self.manager.add_prompt()

            elif choice == "2":
                self.manager.show_prompt_list()

            elif choice == "3":
                self.manager.show_by_category()

            elif choice == "4":
                self.manager.search_prompt()

            elif choice == "5":
                self.manager.show_prompt_detail()

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

#v5까지 해서 커밋해뒀고 git log --oneline --graph --all 로 커밋 잘 됏는지 확인
#git branch로 현재 메인 브랜치에서 작업중인지 확인