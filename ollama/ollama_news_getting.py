import os

# [핵심] 윈도우 환경 변수의 오타를 무시하고 코드가 직접 올바른 주소를 주입합니다.
os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'

import requests
from bs4 import BeautifulSoup
import time
import ollama  # 이제 이 부분에서 에러가 나지 않고 정상 통과합니다.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def get_article_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text().strip() for p in paragraphs])
            return content[:1500]
    except Exception as e:
        print(f"⚠️ 기사 수집 실패 ({url}): {e}")
        return ""


def analyze_trends_with_ollama(news_data):
    prompt = "너는 비즈니스 트렌드 분석가야. 아래 수집된 여러 뉴스 기사 내용을 바탕으로 현재 가장 중요한 핵심 트렌드 3가지를 뽑고 요약해줘.\n\n"
    for i, data in enumerate(news_data, 1):
        prompt += f"[기사 {i}]\n내용: {data}\n\n"
    prompt += "=== 결과 양식 ===\n1. 주요 트렌드 주제\n- 요약 및 분석 내용\n\n한글로 보기 쉽게 정리해줘."

    try:
        print("\n🤖 로컬 AI가 트렌드를 분석하는 중입니다... (대기 시간을 10분으로 늘렸습니다)")

        # 타임아웃을 10분(600초)으로 늘려 안전하게 대기 설정
        client = ollama.Client(timeout=600.0)

        response = client.generate(
            model='gemma4:e4b',
            prompt=prompt
        )
        return response['response']

    except Exception as e:
        return f"❌ AI 분석 실패: {e}."


if __name__ == "__main__":
    news_urls = [
        "https://asiae.co.kr",
        "https://hankyung.com",
        "https://sedaily.com"
    ]

    collected_articles = []
    print("🕸️ 뉴스 기사 수집을 시작합니다...")
    for idx, url in enumerate(news_urls, 1):
        print(f"[{idx}/{len(news_urls)}] 기사 긁어오는 중: {url}")
        content = get_article_content(url)
        if content:
            collected_articles.append(content)
        time.sleep(3)

    if collected_articles:
        analysis_result = analyze_trends_with_ollama(collected_articles)
        print("\n================== 📊 트렌드 분석 보고서 ==================")
        print(analysis_result)
    else:
        print("❌ 수집된 뉴스 기사가 없어 분석을 진행하지 못했습니다.")
