# -*- coding: utf-8 -*-
import os
import sys

# Windows에서 한글 출력을 위한 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ['PYTHONIOENCODING'] = 'utf-8'

try:
    import requests
except ImportError:
    print("requests 라이브러리가 필요합니다. 'pip install requests'를 실행하세요.")
    exit(1)

# .env 파일에서 환경변수 로드 (선택사항)
try:
    from dotenv import load_dotenv
    # 현재 작업 디렉토리에서 .env 파일 로드
    result = load_dotenv()
except ImportError:
    # python-dotenv가 설치되지 않은 경우 무시하고 계속 진행
    pass
except Exception as e:
    # .env 파일 로드 실패 시 무시하고 계속 진행
    pass

import google.generativeai as genai

# --- 사용자 설정 ---
# 1. Google API 키 설정 (환경변수 또는 .env 파일에서 읽어옴)
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("오류: GOOGLE_API_KEY 환경변수가 설정되지 않았습니다.")
    print("다음 중 하나의 방법으로 API 키를 설정하세요:")
    print("1. 환경변수 설정: set GOOGLE_API_KEY=your_api_key (Windows)")
    print("2. .env 파일 생성: python-dotenv 라이브러리 사용")
    print("3. 직접 설정: 코드에서 os.environ['GOOGLE_API_KEY'] = 'your_api_key'")
    exit(1)

genai.configure(api_key=GOOGLE_API_KEY)

# 2. Google Docs 문서 정보
DOCUMENT_ID = "1q56c2rudxEtPqmLsGIUHJbPzYnUJABNemS_sbOyfI1I"
DOCUMENT_NAME = "[샵투식당 RAG_TEST] 레스토랑 메뉴 및 가격"
PDF_FILE_NAME = "shop2rag_menu.pdf"

print("--- 1. Google Docs 문서 다운로드 및 업로드 시작 ---")
print(f"문서 ID: {DOCUMENT_ID}")
print(f"문서명: {DOCUMENT_NAME}")

try:
    # Google Docs 문서를 PDF로 다운로드
    document_url = f"https://docs.google.com/document/d/{DOCUMENT_ID}/export?format=pdf"
    print(f"\n문서를 PDF로 다운로드 중...")
    
    response = requests.get(document_url)
    if response.status_code == 200:
        # PDF 파일로 저장
        with open(PDF_FILE_NAME, 'wb') as f:
            f.write(response.content)
        print(f"다운로드 완료: {PDF_FILE_NAME}")
        
        # 파일 업로드
        print(f"\n파일을 Google AI에 업로드 중...")
        uploaded_file = genai.upload_file(path=PDF_FILE_NAME, display_name=DOCUMENT_NAME)
        print(f"업로드 완료: {uploaded_file.display_name}")
        
        print("\n--- 2. 파일 검색(RAG) 기능으로 모델에 질문하기 ---")
        # 파일 검색 기능을 사용하는 모델 초기화
        model = genai.GenerativeModel(model_name='gemini-2.0-flash-exp')

        # 검색할 질문 (레스토랑 메뉴 관련)
        query = "시그니처 메뉴의 가격을 알려주세요."
        
        # 모델에 질문과 함께 업로드된 파일 전달
        # 라이브러리가 자동으로 파일 내용을 검색하고 컨텍스트로 활용하여 답변을 생성합니다.
        response = model.generate_content([query, uploaded_file])

        print(f"\n질문: {query}")
        print("\n--- 최종 답변 (RAG 적용) ---")
        print(response.text)
        
    else:
        print(f"오류: 문서 다운로드 실패 (상태 코드: {response.status_code})")
        print("문서가 공개되어 있는지 확인하거나, 수동으로 PDF를 다운로드하여 업로드하세요.")
        
except Exception as e:
    print(f"오류 발생: {e}")
    print("\n대안: Google Docs 문서를 수동으로 PDF로 다운로드한 후 업로드하여 사용하세요.")