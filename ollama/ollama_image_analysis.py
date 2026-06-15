import os

# [필수] 윈도우 환경 변수 오류 방지
os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'

import ollama


def analyze_multiple_images_and_suggest_solution(image_paths):
    # AI에게 줄 통합 분석 미션(프롬프트)
    prompt = (
        "너는 대기업 시스템 통합(SI) 및 엔터프라아즈 UX/UI 마스터 컨설턴트야.\n"
        "제공된 여러 장의 그룹웨어 화면 스크린샷은 하나의 업무 흐름으로 연결되어 있어.\n"
        "이 화면들을 종합적으로 연계 분석하여 통합 솔루션 제안서를 작성해줘.\n\n"
        "=== 요구 분석 사항 ===\n"
        "1. 각 화면별(이미지 순서대로) 주요 UI/UX 문제점 요약\n"
        "2. 화면 간 이동(데이터 연동 등)에서 발생하는 비효율성과 단절감 분석\n"
        "3. 전체 업무 속도를 혁신적으로 높이기 위한 통합 시스템 솔루션 아키텍처 제안\n"
        "   - (예: 어떤 신기술 도입, 어떤 메뉴 통합, 어떤 자동화 기능이 필요한지)\n\n"
        "중요한 비즈니스 보고서 양식으로 한글로 깊이 있게 정리해줘."
    )

    try:
        print(f"🖼️ 총 {len(image_paths)}개의 이미지를 확인했습니다. 로컬 AI 통합 분석을 시작합니다...")
        print("💡 여러 장의 이미지를 동시에 분석하므로 시간이 다소 걸릴 수 있습니다.")

        # 타임아웃을 10분(600초)으로 넉넉하게 설정
        client = ollama.Client(timeout=600.0)

        # [핵심] images 리스트에 여러 이미지 경로를 한 번에 주입
        response = client.chat(
            model='gemma4:e4b',
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                    'images': image_paths  # 경로가 담긴 리스트 전달
                }
            ]
        )

        return response['message']['content']

    except Exception as e:
        return f"❌ 통합 이미지 분석 실패: {e}"


if __name__ == "__main__":
    # 분석할 그룹웨어 이미지 파일명들을 순서대로 리스트에 넣습니다.
    # (주의: 파일들이 이 파이썬 파일과 같은 폴더에 존재해야 합니다.)
    groupware_images = [
        "그림1.png",  # 1번: 메인 화면 또는 대시보드
        "그림2.png",  # 2번: 전자결재 화면
        "그림3.png"  # 3번: 상세 내용 입력 화면
    ]

    # 존재하는 파일만 필터링하여 안전하게 진행
    valid_images = [img for img in groupware_images if os.path.exists(img)]

    if len(valid_images) == len(groupware_images):
        analysis_report = analyze_multiple_images_and_suggest_solution(valid_images)
        print("\n================== 📊 그룹웨어 통합 개선 솔루션 제안서 ==================")
        print(analysis_report)
    else:
        missing_files = set(groupware_images) - set(valid_images)
        print(f"❌ 폴더에 없는 파일이 있습니다: {missing_files}")
        print("이미지 파일명을 다시 확인하거나, 경로가 올바른지 체크해 주세요.")
