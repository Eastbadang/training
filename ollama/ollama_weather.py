import os

# [필수] 환경 변수 오류 방지
os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'

import ollama

# ⚠️ 주의: 여기서 사용하는 모델 이름은 실제로 다운로드한 모델명과 일치해야 합니다.
MODEL_NAME = "gemma4:e4b"

def generate_response_simple(prompt):
    # ollama.generate 함수를 사용하여 API를 호출합니다.
    response = ollama.generate(
        model=MODEL_NAME,
        prompt=prompt
    )
    # response 딕셔너리에서 실제로 생성된 텍스트를 추출합니다.
    return response['response']

# 실행
user_prompt = "파이썬으로 날씨를 예측하는 코드를 작성해줘."
result = generate_response_simple(user_prompt)

print("=== 모델 응답 ===")
print(result)
