import os
from tkinter import Tk, filedialog
import pandas as pd


def check_excel_for_csv(file_path):
    """엑셀 파일 1개를 검사하는 함수"""
    print(f"\n🔍 [{os.path.basename(file_path)}] 검사 시작...")

    try:
        df = pd.read_excel(file_path, sheet_name=0)
    except Exception as e:
        print(f"❌ 파일을 열 수 없습니다. 에러 내용: {e}")
        return False

    has_issue = False

    # 1. 빈 칸 확인
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        print(f"  ⚠️ 빈 칸이 {missing_values}개 있습니다.")
        has_issue = True

    # 2. 글자 깨짐 위험 확인
    for col in df.select_dtypes(include=["object"]).columns:
        for idx, value in enumerate(df[col]):
            if pd.notnull(value):
                try:
                    str(value).encode("utf-8")
                except UnicodeEncodeError:
                    print(f"  ❌ 글자 깨짐 위험: [{col}] 열 {idx+2}번째 행")
                    has_issue = True

    # 3. 쉼표(,) 포함 확인
    for col in df.select_dtypes(include=["object"]).columns:
        comma_count = df[col].astype(str).str.contains(",").sum()
        if comma_count > 0:
            print(f"  ⚠️ 쉼표(,) 포함: [{col}] 열에 {comma_count}개")
            has_issue = True

    if not has_issue:
        print("  ✅ 문제없음: CSV로 바꾸기 좋은 깨끗한 데이터입니다.")
    return True


def start_program():
    """사용자에게 선택을 받고 검사를 시작하는 메인 함수"""
    # 팝업창을 띄우기 위한 준비 (뒤에 빈 창이 뜨지 않게 숨김)
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    print("=== 엑셀 파일 검사 프로그램 ===")
    print("1: 여러 파일 직접 고르기")
    print("2: 특정 폴더 안의 모든 엑셀 파일 고르기")

    choice = input("원하는 작업 번호를 입력하고 엔터를 누르세요 (1 또는 2): ").strip()

    file_list = []

    if choice == "1":
        print("\n파일 선택 창이 열립니다. 검사할 엑셀 파일들을 고르세요. (Ctrl 누르고 클릭)")
        # 파일 여러 개 선택창 열기
        files = filedialog.askopenfilenames(
            title="검사할 엑셀 파일들을 선택하세요",
            filetypes=[("Excel Files", "*.xlsx *.xls")],
        )
        file_list = list(files)

    elif choice == "2":
        print("\n폴더 선택 창이 열립니다. 검사할 폴더를 고르세요.")
        # 폴더 선택창 열기
        folder = filedialog.askdirectory(title="엑셀 파일들이 들어있는 폴더를 선택하세요")
        if folder:
            # 폴더 안에서 엑셀 파일만 찾아서 목록에 넣기
            for f in os.listdir(folder):
                if f.endswith((".xlsx", ".xls")) and not f.startswith("~$"):
                    file_list.append(os.path.join(folder, f))

    else:
        print("❌ 잘못된 번호를 입력했습니다. 프로그램을 종료합니다.")
        return

    # 선택된 파일들 검사하기
    if not file_list:
        print("선택된 엑셀 파일이 없습니다.")
        return

    print(f"\n총 {len(file_list)}개의 파일을 검사합니다.")
    for file in file_list:
        check_excel_for_csv(file)

    print("\n🎉 모든 파일 검사가 완료되었습니다!")


# 프로그램 실행
if __name__ == "__main__":
    start_program()
