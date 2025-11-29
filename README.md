# Shop2RAG - Google 파일 검색 API를 활용한 RAG 시스템

[![YouTube Video](https://img.youtube.com/vi/S5Zr_Pw6xNM/maxresdefault.jpg)](https://www.youtube.com/watch?v=S5Zr_Pw6xNM)

Google의 파일 검색 스토어(FileSearchStore)를 활용하여 RAG(Retrieval-Augmented Generation) 시스템을 구축하는 Python 예제입니다.

## 📋 개요

이 프로젝트는 Google Docs 문서를 업로드하고, 파일 검색 API를 통해 문서 내용에 대해 질문하여 RAG 기반의 답변을 얻는 과정을 보여줍니다.

### 주요 기능

- Google Docs 문서를 PDF로 자동 다운로드
- Google AI의 파일 검색 스토어에 업로드
- 자동 청크 분할 및 인덱싱
- 의미 기반 검색을 통한 RAG 질의-응답

## 🚀 시작하기

### 1. 사전 준비

#### Google API 키 발급
1. [Google AI Studio](https://aistudio.google.com/api-keys)에 접속
2. API 키 생성
3. 생성된 API 키를 복사

#### 필요한 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 설정

#### 방법 1: 환경변수 사용 (권장)

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**Windows (CMD):**
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

#### 방법 2: .env 파일 사용

1. `.env.example` 파일을 `.env`로 복사:
```bash
cp .env.example .env
```

2. `.env` 파일을 열어 API 키 입력:
```
GOOGLE_API_KEY=your_api_key_here
```

3. 코드에서 `python-dotenv` 사용 (선택사항):
```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. 실행

```bash
python shop2rag.py
```

## 📖 사용 방법

### 기본 사용

코드를 실행하면 기본 설정으로 Google Docs 문서를 다운로드하고 질문에 답변합니다.

### 커스터마이징

`shop2rag.py` 파일에서 다음 변수들을 수정할 수 있습니다:

```python
# Google Docs 문서 ID
DOCUMENT_ID = "your_document_id_here"

# 문서 표시 이름
DOCUMENT_NAME = "문서 이름"

# 질문 내용
query = "원하는 질문을 입력하세요."
```

## 🔍 RAG 동작 원리

이 코드는 Google의 파일 검색 스토어를 활용한 RAG 시스템입니다.

### 전체 흐름

1. **문서 준비**: Google Docs 문서를 PDF로 다운로드
2. **FileSearchStore 업로드**: 파일을 업로드하면 자동으로 전처리 및 청크 분할 수행
3. **검색 (Retrieval)**: 질문과 관련된 문서 청크를 의미 기반으로 검색
4. **증강 (Augmentation)**: 검색된 청크를 컨텍스트로 준비
5. **생성 (Generation)**: Gemini 모델이 컨텍스트와 질문을 바탕으로 답변 생성

자세한 내용은 [RAG_동작원리_설명.md](./RAG_동작원리_설명.md)를 참고하세요.

### 파일 검색 스토어

[Google 파일 검색 스토어 문서](https://ai.google.dev/api/file-search/file-search-stores?hl=ko)에 따르면:

- **FileSearchStore**는 Document들의 모음으로, RAG 시스템을 위한 호스팅 질의 응답 서비스를 제공합니다
- `uploadToFileSearchStore` 메서드를 통해 자동으로 전처리 및 청크 분할이 수행됩니다
- 의미 기반 검색을 통해 관련 문서를 효율적으로 찾아냅니다

## 📁 프로젝트 구조

```
rag-python/
├── shop2rag.py              # 메인 실행 파일
├── requirements.txt         # 필요한 라이브러리 목록
├── .env.example            # 환경변수 예제 파일
├── .gitignore              # Git 제외 파일 목록
├── README.md               # 프로젝트 설명서
└── RAG_동작원리_설명.md    # RAG 동작 원리 상세 설명
```

## ⚙️ 설정 옵션

### 모델 변경

현재는 `gemini-2.0-flash-exp` 모델을 사용합니다. 다른 모델로 변경하려면:

```python
model = genai.GenerativeModel(model_name='gemini-1.5-pro')
```

### 문서 접근 권한

Google Docs 문서가 공개되어 있어야 자동 다운로드가 가능합니다. 비공개 문서의 경우:
1. 문서를 PDF로 수동 다운로드
2. 같은 디렉토리에 저장
3. `DOCUMENT_ID` 대신 파일 경로 사용

## 🔒 보안 주의사항

⚠️ **중요**: API 키는 절대 GitHub에 업로드하지 마세요!

- `.env` 파일은 `.gitignore`에 포함되어 있습니다
- 환경변수나 `.env` 파일을 통해 API 키를 관리하세요
- API 키가 노출되면 즉시 재발급 받으세요

## 📚 참고 자료

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API 문서](https://ai.google.dev/docs)
- [파일 검색 스토어 API](https://ai.google.dev/api/file-search/file-search-stores?hl=ko)

## 🤝 기여

이슈나 개선 사항이 있으면 언제든지 제안해주세요!

## 📄 라이선스

이 프로젝트는 예제 코드로 제공됩니다.
