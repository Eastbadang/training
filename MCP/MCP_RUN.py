# mcp_client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_mcp_client():
    # 1. 실행할 서버 설정 (위에서 만든 파일 지정)
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_ex00.py"]
    )

    # 2. 서버에 연결 및 세션 시작
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 3. 서버가 제공하는 도구 목록 확인
            tools = await session.list_tools()
            print(f"사용 가능한 도구: {tools}")

            # 4. 도구 호출 (서울 날씨 조회)
            result = await session.call_tool("get_weather", arguments={"city": "수원"})
            print(f"결과: {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(run_mcp_client())
