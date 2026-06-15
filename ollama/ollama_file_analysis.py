import os

# [필수] 환경 변수 오류 방지
os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'

import ollama
from pypdf import PdfReader
from docx import Document


# 1. PDF 파일에서 글자만 추출하는 함수
def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"PDF 읽기 실패: {e}"


# 2. 워드 파일(.docx)에서 글자만 추출하는 함수
def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Word 읽기 실패: {e}"


# 3. 한글 파일(.hwp)에서 글자만 추출하는 함수 (인코딩 처리)
def extract_text_from_hwp(file_path):
    try:
        # 한글 파일은 바이너리를 텍스트로 강제 변환하여 문자열만 필터링
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()[:5000]  # 특수 포맷 제외 글자만 일부 추출
    except Exception as e:
        return f"한글 파일 읽기 실패: {e}"


# 4. 추출한 텍스트를 파일 첨부 없이 Ollama로 분석하는 함수
def analyze_file_content_with_ollama(file_text):
    prompt = (
        "너는 전기차(EV) 충전 인프라 전문 비즈니스 분석가야.\n"
        "아래 제공된 문서 내용을 분석하여, '전기차 유선충전' 및 '무선충전' 기술/시장 분야에 집중해서 핵심 내용을 요약해줘.\n\n"
        f"[문서 내용]\n{file_text[:3000]}\n\n"  # 너무 길면 AI가 과부하 걸리므로 3000자 제한
        "=== 결과 양식 ===\n"
        "1. 문서 내 유/무선 충전 핵심 요약\n"
        "- 요점 작성\n\n"
        "2. 우리 업무에 적용할 시사점\n"
        "- 전략적 의견 작성"
    )

    try:
        print("\n🤖 로컬 AI가 파일 내용을 분석하는 중입니다...")
        client = ollama.Client(timeout=600.0)
        response = client.generate(
            model='gemma4:e4b',
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"❌ AI 분석 실패: {e}."


# 🚀 메인 실행부
if __name__ == "__main__":
    # 분석하고 싶은 파일의 이름과 확장자를 적어주세요.
    # (주의: 파일이 이 파이썬 스크립트와 같은 폴더에 있어야 합니다)
    file_name = "추출 파일 이름.pdf"

    print(f"📁 [{file_name}] 파일에서 글자를 추출하는 중...")

    # 확장자에 맞게 글자 추출기 작동
    extracted_text = ""
    if file_name.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_name)
    elif file_name.endswith('.docx'):
        extracted_text = extract_text_from_docx(file_name)
    elif file_name.endswith('.hwp'):
        extracted_text = extract_text_from_hwp(file_name)

    # 글자가 정상적으로 추출되었다면 파일 첨부 없이 Ollama에 문장으로 전달
    if extracted_text.strip() and "실패" not in extracted_text:
        print("📝 글자 추출 성공! AI 분석을 시작합니다.")
        analysis_result = analyze_file_content_with_ollama(extracted_text)
        print("\n================== 📊 로컬 파일 분석 보고서 ==================")
        print(analysis_result)
    else:
        print(f"❌ 파일을 읽지 못했거나 내용이 없습니다. 오류 메시지: {extracted_text}")
