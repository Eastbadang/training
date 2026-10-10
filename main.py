import os
from google import genai

# Secrets에 등록된 환경 변수에서 안전하게 키를 읽어옵니다.
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="GitHub Actions에서 보낸 테스트 메시지입니다. 짧게 인사해 줘.",
)

print(response.text)
