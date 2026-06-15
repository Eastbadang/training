import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def scroll_down_slowly(driver):
    """요소가 로드될 수 있도록 페이지를 더 세밀하게 스크롤합니다."""
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    current_pos = 0
    while current_pos < total_height:
        driver.execute_script(f"window.scrollTo(0, {current_pos});")
        current_pos += viewport_height
        time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


def crawl_ces_updated():
    driver = get_driver()
    all_data = []

    # 설정 데이터
    config = {
        2024: 30, # 472개 (30페이지)
        2025: 29, # 458개 (29페이지
        2026: 29  # 452개 (29페이지)
    }

    try:
        for year, max_page in config.items():
            for page in range(1, max_page + 1):
                url = f"https://www.ces.tech/ces-innovation-awards/?year={year}&page={page}"
                print(f"\n--- {year}년 {page}페이지 접속 중 ---")

                driver.get(url)

                try:
                    # 페이지 로딩 대기
                    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                    # 2025년 누락 방지를 위한 전체 스크롤
                    scroll_down_slowly(driver)

                    # 카드 추출 (Raw string 사용)
                    cards = driver.find_elements(By.CSS_SELECTOR, r"div.group\/card")

                    if not cards:
                        print(f"   [정보] {year}년 {page}페이지에 제품 카드가 없습니다.")
                        break

                    page_items = []
                    for card in cards:
                        try:
                            # 텍스트 추출 방식 변경: .text 대신 get_attribute("textContent") 사용 (숨겨진 텍스트 대응)
                            # 회사명: h3 또는 .f-heading-4
                            company_el = card.find_elements(By.CSS_SELECTOR, "h3, .f-heading-4")
                            company = company_el[0].get_attribute("textContent").strip() if company_el else "N/A"

                            # 제품명: p 또는 .f-body-3
                            product_el = card.find_elements(By.CSS_SELECTOR, "p, .f-body-3")
                            product = product_el[0].get_attribute("textContent").strip() if product_el else "N/A"

                            # 링크: a 태그
                            link_el = card.find_elements(By.TAG_NAME, "a")
                            link = link_el[0].get_attribute("href") if link_el else ""

                            if company != "N/A" and product != "N/A":
                                page_items.append([year, company, product, link])
                        except Exception:
                            continue

                    # 한 페이지 16개 기준 중복(추천항목 4개) 제거 logic
                    # 추천 항목이 앞에 나오므로 뒤에서 16개를 취하거나, 나중에 전체 중복 제거 수행
                    all_data.extend(page_items)
                    print(f"   -> {year}년 {page}페이지: {len(page_items)}개 감지됨")

                except Exception as e:
                    print(f"   [에러] {year}년 {page}페이지 처리 중 오류 발생")
                    continue

                # 테스트 시 각 연도 1페이지만 하려면 아래 break 해제
                # break

    finally:
        driver.quit()

    if all_data:
        # 데이터프레임 생성
        df = pd.DataFrame(all_data, columns=['연도', '회사명', '제품명', '링크'])

        # 1. 중복 제거 (추천 항목 4개가 중복으로 들어오는 경우 방지)
        df = df.drop_duplicates(subset=['회사명', '제품명'], keep='last')

        # 2. 엑셀 하이퍼링크 적용 저장
        file_name = "CES_Innovation_Awards_2024_2026_Hyperlinked.xlsx"

        # xlsxwriter 엔진 사용
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='CES_Awards')

        workbook = writer.book
        worksheet = writer.sheets['CES_Awards']

        # 링크 열(D열)을 파란색 하이퍼링크 스타일로 변경
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1})
        link_format = workbook.add_format({'font_color': 'blue', 'underline': 1})

        # 데이터 쓰기 (하이퍼링크 공식 적용)
        for row_num, link_url in enumerate(df['링크'], start=1):
            if link_url:
                # 엑셀 공식: =HYPERLINK("URL", "클릭하여 이동")
                worksheet.write_url(row_num, 3, link_url, link_format, string="바로가기")
            else:
                worksheet.write(row_num, 3, "N/A")

        writer.close()
        print(f"\n========================================")
        print(f"최종 저장 완료: {file_name}")
        print(f"최종 데이터 개수: {len(df)}건")
        print(f"========================================")
    else:
        print("수집된 데이터가 없습니다.")


if __name__ == "__main__":
    crawl_ces_updated()
