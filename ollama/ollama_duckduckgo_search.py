import os

# [필수] 환경 변수 오류 방지
os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'

import ollama
from duckduckgo_search import DDGS


def search_web(query):
    """실시간 웹 검색 수행"""
    print(f"🔍 '{query}' 검색 중...")
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            results.append(f"제목: {r['title']}\n내용: {r['body']}")
    return "\n\n".join(results)


def ask_with_search(user_question):
    # 1. 웹 검색 수행
    search_context = search_web(user_question)

    # 2. 프롬프트 구성 (검색 결과 + 사용자 질문)
    prompt = f"""
    당신은 실시간 정보를 분석하는 AI 도우미입니다. 
    제공된 [검색 결과]를 바탕으로 [사용자 질문]에 대해 최신 정보를 포함하여 친절하게 답변하세요.
    반드시 검색 결과에 근거하여 답변하고, 모르는 내용은 추측하지 마세요.

    [검색 결과]
    {search_context}

    [사용자 질문]
    {user_question}
    """

    # 3. Ollama 모델 호출 (예: llama3.1 또는 gemma2)
    print("🤖 AI가 정보를 분석 중입니다...")
    response = ollama.chat(model="gemma4:e4b", messages=[
        {'role': 'user', 'content': prompt},
    ])

    return response['message']['content']


# 실행 예시
if __name__ == "__main__":
    question = "오늘의 삼성전자 주가 흐름과 주요 뉴스 요약해줘"
    answer = ask_with_search(question)
    print("\n--- 분석 결과 ---")
    print(answer)
