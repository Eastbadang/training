import requests
from bs4 import BeautifulSoup
import csv
import time


def get_last_page(session, base_url, headers):
    """하단 페이지네이션에서 마지막 페이지 번호를 추출합니다."""
    try:
        response = session.get(base_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # '맨 뒤로' 가기 버튼이나 페이지 번호 중 가장 큰 값을 찾음
        # 보통 .paging 클래스 내의 마지막 a 태그 혹은 href의 page= 숫자를 추출
        paging_links = soup.select('.paging a[href*="page="]')
        if not paging_links:
            return 32  # 찾지 못할 경우 기본값 설정

        page_nums = []
        for link in paging_links:
            href = link.get('href')
            # 'page=숫자' 부분에서 숫자만 추출
            import re
            match = re.search(r'page=(\[0-9]+)', href)
            if match:
                page_nums.append(int(match.group(1)))

        return max(page_nums) if page_nums else 32
    except:
        return 32  # 오류 발생 시 넉넉하게 32페이지로 기본 설정


def scrape_kar_members():
    all_members = []
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://www.korearobot.or.kr'
    }

    base_url = "https://www.korearobot.or.kr/member/status.htm?page=1&msg=#filter_anchor"

    # 1. 마지막 페이지 번호 자동 확인
    last_page = get_last_page(session, base_url, headers)
    print(f"감지된 마지막 페이지: {last_page}페이지. 수집을 시작합니다...")

    # 2. 1페이지부터 마지막 페이지까지 유동적으로 반복
    page = 1
    while page <= last_page:
        url = f"{base_url}?page={page}&msg=#filter_anchor"

        try:
            response = session.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'html.parser')

            # 회원사 박스 추출 (.box.mem01 등 가변 클래스 대응)
            member_boxes = soup.select('.box.mem01, .box.mem02, .box')

            # 만약 해당 페이지에 데이터가 없으면 수집 종료
            if not member_boxes:
                print(f"[{page}페이지] 더 이상 데이터가 없습니다. 수집을 종료합니다.")
                break

            current_page_count = 0
            for box in member_boxes:
                # 1. 회사명과 회원구분이 들어있는 영역
                name_div = box.select_one('.name')
                if not name_div: continue

                member_type = name_div.select_one('span').get_text(strip=True) if name_div.select_one('span') else "N/A"
                company_name = name_div.select_one('strong').get_text(strip=True) if name_div.select_one(
                    'strong') else "N/A"

                # 2. 기업규모 추출 (5번째 dd 태그)
                # box 내의 모든 dd 태그를 리스트로 가져옵니다.
                all_dd = box.select('dd')

                # 인덱스는 0부터 시작하므로 5번째는 [4]입니다.
                # 데이터가 부족할 경우를 대비해 길이를 체크합니다.
                company_size = all_dd[4].get_text(strip=True) if len(all_dd) >= 5 else "N/A"

                # 3. 홈페이지 링크
                link_tag = box.select_one('a.link_homepage')
                homepage = link_tag['href'] if link_tag and link_tag.has_attr('href') else "N/A"

                if company_name != "N/A":
                    all_members.append({
                        '회원구분': member_type,
                        '회사명': company_name,
                        '기업규모': company_size,  # 이제 5번째 dd의 값이 들어갑니다.
                        '홈페이지': homepage
                    })
                    current_page_count += 1

            print(f"[{page}/{last_page} 페이지] 완료 - {current_page_count}개 추출 (누적: {len(all_members)}개)")

            page += 1
            time.sleep(0.6)  # 서버 부하 방지

        except Exception as e:
            print(f"[{page}페이지] 오류 발생: {e}")
            break

    # 3. 결과 저장
    save_to_csv(all_members)


def save_to_csv(data):
    if not data:
        print("\n데이터가 수집되지 않았습니다.")
        return

    filename = 'kar_members_dynamic.csv'
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['회원구분', '회사명', '기업규모', '홈페이지'])
        writer.writeheader()
        writer.writerows(data)
    print(f"\n성공! 총 {len(data)}건의 회원사 정보를 '{filename}'에 저장했습니다.")


if __name__ == "__main__":
    scrape_kar_members()
