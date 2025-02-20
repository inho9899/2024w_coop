# 🖼 AI 기반 텍스트 & 이미지 생성기

이 프로젝트는 **Flask + Streamlit + Diffusers**를 활용하여 **텍스트 및 이미지 생성이 가능한 AI 웹 애플리케이션**입니다. 사용자는 **LLM 기반 텍스트 생성** 및 **Stable Diffusion을 활용한 이미지 생성**을 수행할 수 있습니다.

## 📌 프로젝트 개요

- **백엔드:** Flask (FastAPI 기반)
- **프론트엔드:** Streamlit (웹 UI 제공)
- **텍스트 생성:** Hugging Face Transformers (GPT-2 기반 모델 활용)
- **이미지 생성:** Diffusers (Stable Diffusion 모델 활용)
- **실행 환경:** WSL 또는 Linux (GPU 지원 가능)

---

## 🚀 기능 소개

### ✅ 텍스트 생성 기능 (`/generate_text`)

- 사용자가 입력한 프롬프트를 바탕으로 **LLM이 자연스러운 텍스트를 생성**합니다.
- 사용 모델: `distilgpt2` (경량 GPT-2 기반)

### ✅ 이미지 생성 기능 (`/generate_image`)

- 사용자가 입력한 텍스트 프롬프트를 바탕으로 **Stable Diffusion을 활용해 이미지 생성**합니다.
- 사용 모델: `CompVis/stable-diffusion-v1-4`

---

## 📂 프로젝트 디렉토리 구조

```
project_ai/
 ├── app/
 │   ├── server.py         # Flask 백엔드 API
 │   ├── app.py            # Streamlit UI (프론트엔드)
 │   ├── requirements.txt  # Python 라이브러리 목록
 │
 ├── models/               # Hugging Face 모델 캐시 폴더
 │
 ├── data/                 # 생성된 이미지 저장 폴더
 │
 ├── README.md             # 프로젝트 설명 파일
```

---

## 🔧 설치 및 실행 방법

### **1️⃣ 필수 라이브러리 설치**

```bash
pip install -r app/requirements.txt
```

### **2️⃣ Flask 서버 실행**

```bash
cd app
python3 server.py
```

### **3️⃣ Streamlit 프론트엔드 실행**

```bash
cd app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### **4️⃣ 실행 후 확인할 URL**

- **Flask API**: `http://localhost:5000`
- **Streamlit UI**: `http://localhost:8501`

---

## 🛠 API 엔드포인트

### \*\*1️⃣ 텍스트 생성 (`/generate_text`)

- **요청 방식:** `POST`
- **요청 데이터(JSON):**
  ```json
  {"prompt": "Write a short fantasy story"}
  ```
- **응답 데이터(JSON):**
  ```json
  {"generated_text": "Once upon a time in a distant kingdom..."}
  ```

### \*\*2️⃣ 이미지 생성 (`/generate_image`)

- **요청 방식:** `POST`
- **요청 데이터(JSON):**
  ```json
  {"prompt": "A futuristic city at sunset"}
  ```
- **응답 데이터:** 생성된 이미지 (`image/png` 포맷)

---

## 🖼 예제 실행 결과

### 🔹 텍스트 생성 예시

**입력:** `"Describe a medieval castle"`

**출력:**

> "A grand fortress with towering stone walls and intricate battlements..."

### 🔹 이미지 생성 예시

**입력:** `"A mystical forest with glowing trees"`

**출력:**&#x20;

---

## 📌 참고 및 추가 설정

- **CUDA 지원 여부 확인:** `torch.cuda.is_available()`
- 모델 다운로드 속도를 높이려면 Hugging Face 계정 로그인 필요:
  ```bash
  huggingface-cli login
  ```

---


