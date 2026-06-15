import os
import pandas as pd
from tkinter import Tk, filedialog


def excel_to_csv_sheets():
    # tkinter 윈도우 창 숨기기 설정
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # 선택 창을 화면 맨 앞으로 가져옴

    # 1. 엑셀 파일 선택
    print("변환할 엑셀 파일을 선택하는 중...")
    excel_path = filedialog.askopenfilename(
        title="변환할 엑셀 파일을 선택하세요",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )

    if not excel_path:
        print("엑셀 파일 선택이 취소되었습니다.")
        return

    # 2. 저장할 폴더 선택
    print("CSV 파일을 저장할 폴더를 선택하는 중...")
    save_dir = filedialog.askdirectory(title="CSV 파일을 저장할 폴더를 선택하세요")

    if not save_dir:
        print("저장 폴더 선택이 취소되었습니다.")
        return

    try:
        # 입력 파일명 추출 (확장자 제외)
        base_name = os.path.splitext(os.path.basename(excel_path))[0]

        # 엑셀 파일의 모든 시트 읽기 (sheet_name=None으로 설정 시 딕셔너리 형태로 반환)
        print(f"\n데이터를 읽는 중: {base_name}")
        excel_file = pd.read_excel(excel_path, sheet_name=None)

        print("\n--- CSV 변환 시작 ---")
        # 시트별로 순회하며 CSV로 저장
        for sheet_name, df in excel_file.items():
            # 파일명 자동 구성: 저장파일명_시트명.csv
            # 한글 시트명이 깨지지 않도록 안전하게 구성합니다.
            csv_filename = f"{base_name}_{sheet_name}.csv"
            csv_path = os.path.join(save_dir, csv_filename)

            # CSV 저장 (인코딩은 엑셀에서 한글이 깨지지 않도록 'utf-8-sig' 사용)
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            print(f"저장 완료: {csv_filename}")

        print("\n모든 시트가 성공적으로 CSV 파일로 분할 저장되었습니다! 🎉")

    except Exception as e:
        print(f"\n작업 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    excel_to_csv_sheets()
