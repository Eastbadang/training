import requests
from bs4 import BeautifulSoup
import csv
import time
import re

def get_last_page(session, headers):
    """하단 페이지네이션에서 마지막 페이지 번호를 추출합니다."""
    # 페이지 번호가 없는 기본 목록 주소 사용
    list_url = "https://www.korearobot.or.kr/member/status.htm?page=1&msg=#filter_anchor"
    try:
        response = session.get(list_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # '맨 뒤로' 가기 버튼이나 페이지 번호 중 가장 큰 값을 찾음
        paging_links = soup.select('.paging a[href*="page="]')
        if not paging_links:
            return 32

        page_nums = []
        for link in paging_links:
            href = link.get('href')
            # 숫자만 추출하는 정규식 수정 (\d+)
            match = re.search(r'page=(\d+)', href)
            if match:
                page_nums.append(int(match.group(1)))

        return max(page_nums) if page_nums else 32
    except:
        return 32

def scrape_kar_members():
    all_members = []
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    # 1. 마지막 페이지 번호 자동 확인
    last_page = get_last_page(session, headers)
    print(f"감지된 마지막 페이지: {last_page}페이지. 수집을 시작합니다...")

    # 2. 1페이지부터 마지막 페이지까지 반복
    for page in range(1, last_page + 1):
        # URL 생성 시 중복된 ?나 page 파라미터가 없도록 구성
        url = f"https://www.korearobot.or.kr/member/status.htm?page={page}&msg=#filter_anchor"

        try:
            response = session.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'html.parser')
            # 회원사 박스 선택자
            member_boxes = soup.select('.box')

            if not member_boxes:
                print(f"[{page}페이지] 데이터가 없습니다. 종료합니다.")
                break

            current_page_count = 0
            for box in member_boxes:
                name_div = box.select_one('.name')
                if not name_div: continue

                member_type = name_div.select_one('span').get_text(strip=True) if name_div.select_one('span') else "N/A"
                company_name = name_div.select_one('strong').get_text(strip=True) if name_div.select_one('strong') else "N/A"

                # 기업규모 (dd 태그 중 '기업규모' 텍스트를 포함한 것을 찾는 것이 더 정확함)
                all_dd = box.select('dd')
                company_size = "N/A"
                if len(all_dd) >= 5:
                    company_size = all_dd[4].get_text(strip=True)

                # 홈페이지 링크
                link_tag = box.select_one('a.link_homepage')
                homepage = link_tag['href'] if link_tag and link_tag.has_attr('href') else "N/A"

                if company_name != "N/A":
                    all_members.append({
                        '회원구분': member_type,
                        '회사명': company_name,
                        '기업규모': company_size,
                        '홈페이지': homepage
                    })
                    current_page_count += 1

            print(f"[{page}/{last_page} 페이지] 완료 - {current_page_count}개 추출 (누적: {len(all_members)}개)")
            time.sleep(0.8) # 차단 방지를 위해 약간의 여유를 둡니다.

        except Exception as e:
            print(f"[{page}페이지] 오류 발생: {e}")
            continue # 오류 시 다음 페이지 시도

    save_to_csv(all_members)

def save_to_csv(data):
    if not data:
        print("\n데이터가 없습니다.")
        return

    filename = 'kar_members_fixed.csv'
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['회원구분', '회사명', '기업규모', '홈페이지'])
        writer.writeheader()
        writer.writerows(data)
    print(f"\n성공! 총 {len(data)}건 저장 완료: {filename}")

if __name__ == "__main__":
    scrape_kar_members()
