# mcp_server.py
from mcp.server.fastmcp import FastMCP
import requests

# 1. MCP 서버 객체 생성
mcp = FastMCP("WeatherService")

# 2. LLM이 사용할 도구(Tool) 정의
@mcp.tool()
def get_weather(city: str) -> str:
    """특정 도시의 현재 날씨 정보를 가져옵니다."""
    # 실제 환경에서는 OpenWeatherMap 등의 API 키를 사용하세요.
    # 여기서는 예시를 위해 간단한 가상 응답을 반환합니다.
    return f"{city}의 현재 날씨는 맑음, 기온은 22도입니다."

# 3. 서버 실행
if __name__ == "__main__":
    mcp.run()
