**✅ AI 면접 시스템 직접 학습 프로젝트 계획 (5월 완료 목표)**

📅 **프로젝트 기간: 2024년 3월 ~ 2024년 5월**  
🎯 **목표: GPT-4, Whisper 등 API 없이 오픈소스 AI 모델을 활용한 AI 면접 시스템 구축**  

---

## **📌 1. 프로젝트 개요**
### **🔹 주요 기능**
1️⃣ **STT (음성 → 텍스트 변환)** → **Librosa + Wav2Vec 2.0 사용**  
2️⃣ **NLP 기반 답변 평가** → **TF-IDF + SVM 또는 BERT 학습**  
3️⃣ **표정 분석 (감정 인식)** → **OpenCV + CNN (Keras) 학습**  
4️⃣ **시선 추적 (면접 태도 분석)** → **MediaPipe + OpenCV 사용**  
5️⃣ **최종 점수 계산 & 피드백** → **Pandas + Scikit-learn 활용**  

### **🔹 개발 환경 및 기술 스택**
- **프로그래밍 언어:** Python, TypeScript
- **백엔드:** FastAPI, MySQL, SQLAlchemy
- **프론트엔드:** React, TypeScript, Tailwind CSS
- **딥러닝 프레임워크:** TensorFlow/Keras, PyTorch
- **머신러닝 라이브러리:** Scikit-learn, Pandas, NumPy
- **음성 처리:** Librosa, Pydub, FFmpeg
- **영상 분석:** OpenCV, MediaPipe, Dlib
- **데이터 저장:** MySQL (면접 결과 저장)
- **배포:** 추후 협의 후 확정 예정

---

## **📌 2. 프로젝트 일정 (2024년 3월 ~ 5월, 팀원별 세부 일정 포함)**

### **🟢 3월 (프로젝트 초기 설정 및 데이터 수집)**
✅ **1주차 (3/1 ~ 3/7): 프로젝트 환경 구축**
- [ ] **(김태현 - AI 개발)** Librosa, TensorFlow, OpenCV 설치 및 환경 구성
- [ ] **(정주훈 - 백엔드 개발)** FastAPI, MySQL, SQLAlchemy 개발 환경 세팅 및 기본 API 설계
- [ ] **(임윤섭 - 프론트엔드 개발)** React + TypeScript + Tailwind CSS 프로젝트 설정 및 기본 UI 레이아웃 구성
- [ ] **(전체 팀)** GitHub 저장소 생성 및 협업 환경 설정

✅ **2주차 (3/8 ~ 3/14): 데이터셋 수집 및 정리**
- [ ] **(김태현 - AI 개발)** STT 학습용 음성 데이터 수집 (LibriSpeech, Mozilla Common Voice 활용) 및 전처리
- [ ] **(김태현 - AI 개발)** NLP 답변 분석을 위한 면접 답변 데이터셋 구축
- [ ] **(김태현 - AI 개발)** 표정 감정 분석을 위한 이미지 데이터셋 구축 (FER2013 활용 가능)
- [ ] **(정주훈 - 백엔드 개발)** MySQL 테이블 설계 및 DB 모델링
- [ ] **(임윤섭 - 프론트엔드 개발)** 기본적인 UI 컴포넌트 정의 및 로그인 페이지 UI 구현

✅ **3주차 (3/15 ~ 3/21): AI 모델 초기 설정 및 기본 백엔드 구축**
- [ ] **(김태현 - AI 개발)** Wav2Vec 2.0 모델 다운로드 및 기본 학습 시작
- [ ] **(김태현 - AI 개발)** NLP 분석을 위한 TF-IDF + SVM 모델 구축
- [ ] **(김태현 - AI 개발)** OpenCV + CNN 기반 감정 분석 모델 초기 설정
- [ ] **(정주훈 - 백엔드 개발)** FastAPI 기본 API 엔드포인트 구축 (회원가입, 로그인, 면접 기록 저장)
- [ ] **(임윤섭 - 프론트엔드 개발)** 로그인 및 회원가입 UI 구현, Tailwind CSS 적용 및 스타일링

✅ **4주차 (3/22 ~ 3/31): 데이터 전처리 및 모델 튜닝**
- [ ] **(김태현 - AI 개발)** 음성 데이터 정리 및 STT 모델 학습 시작
- [ ] **(김태현 - AI 개발)** NLP 모델을 학습할 데이터 정리 및 벡터화
- [ ] **(김태현 - AI 개발)** 감정 분석 모델 (CNN) 학습 데이터 생성
- [ ] **(정주훈 - 백엔드 개발)** FastAPI와 MySQL 연동 테스트, API 속도 최적화
- [ ] **(임윤섭 - 프론트엔드 개발)** UI 디자인 개선 및 API 연동 구현

---

### **🟡 4월 (모델 학습 및 백엔드 & 프론트엔드 기능 확장)**
✅ **5주차 (4/1 ~ 4/7): STT 모델 학습 및 성능 평가**
✅ **6주차 (4/8 ~ 4/14): NLP 기반 답변 평가 모델 학습**
✅ **7주차 (4/15 ~ 4/21): 표정 분석 및 시선 추적 모델 학습**
✅ **8주차 (4/22 ~ 4/30): 모델 통합 및 백엔드-프론트엔드 연결**

**(각 주차별 팀원 역할 추가)**
- [ ] **(김태현 - AI 개발)** AI 모델 학습, 튜닝, 성능 평가
- [ ] **(정주훈 - 백엔드 개발)** API 최적화, 면접 진행 로직 구현 (질문 생성 및 답변 저장 API 추가)
- [ ] **(임윤섭 - 프론트엔드 개발)** 면접 진행 UI 개발, 음성 녹음 및 시각화 기능 구현

---

### **🔴 5월 (최적화 및 시스템 배포)**
✅ **9주차 (5/1 ~ 5/7): 모델 최적화 및 속도 개선**
✅ **10주차 (5/8 ~ 5/14): 웹 인터페이스 및 결과 저장 시스템 구축**
✅ **11주차 (5/15 ~ 5/21): 최종 테스트 및 버그 수정**
✅ **12주차 (5/22 ~ 5/31): 프로젝트 최종 완료 및 문서화**

---

## **📌 3. 팀원 역할 분배 (전체 일정 반영)**
| 역할 | 담당자 | 주요 업무 |
|------|------|--------|
| **AI 개발 (음성, NLP, 영상 분석)** | 김태현 | Wav2Vec 2.0, NLP 모델, OpenCV 기반 감정 분석 모델 학습 및 최적화 |
| **백엔드 개발 (FastAPI, DB 관리)** | 정주훈 | FastAPI 서버 구축, MySQL 연동, AI 모델 API 개발 및 최적화, 면접 진행 로직 구현 |
| **프론트엔드 개발 (React, UI/UX)** | 임윤섭 | React + TypeScript + Tailwind CSS UI 개발, API 연동, 음성 녹음 기능 추가 |

---

✅ **현재까지 진행한 과정에서 가상환경(venv)에 설치한 패키지 목록을 정리해드릴게요.**  
📌 **이 패키지들은 AI 모델 학습, 데이터 전처리, API 구축을 위해 설치한 것들입니다.**  

### **1️⃣ 기본 환경 설정 (FastAPI + 데이터베이스)**
```bash
pip install fastapi uvicorn sqlalchemy pymysql passlib python-jose
```
✔ `fastapi` → FastAPI 웹 프레임워크  
✔ `uvicorn` → FastAPI 실행 서버  
✔ `sqlalchemy` → MySQL ORM (데이터베이스 연결)  
✔ `pymysql` → MySQL 연결  
✔ `passlib` → 비밀번호 해싱  
✔ `python-jose` → JWT 토큰 생성  

---

### **2️⃣ AI 모델 학습을 위한 패키지**
```bash
pip install torch torchaudio transformers librosa soundfile numpy pandas
```
✔ `torch` / `torchaudio` → PyTorch 및 오디오 처리  
✔ `transformers` → Wav2Vec 2.0, NLP 모델 사용  
✔ `librosa` → 오디오 데이터 처리  
✔ `soundfile` → 오디오 파일 변환  
✔ `numpy` → 데이터 연산  
✔ `pandas` → 데이터프레임 관리  

---

### **3️⃣ OpenCV 및 영상 분석 (표정, 시선 분석)**
```bash
pip install opencv-python mediapipe tensorflow keras
```
✔ `opencv-python` → 이미지 처리  
✔ `mediapipe` → 시선 추적 및 얼굴 감지  
✔ `tensorflow` / `keras` → 표정 분석 CNN 모델  

---

### **4️⃣ 데이터 전처리 및 AI 평가 모델**
```bash
pip install scikit-learn datasets
```
✔ `scikit-learn` → NLP 데이터 분석 (TF-IDF, SVM 등)  
✔ `datasets` → NLP 모델 학습 데이터 다운로드  

---

### **5️⃣ API 호출 및 인증 관련**
```bash
pip install requests httpx
```
✔ `requests` → API 호출  
✔ `httpx` → 비동기 API 호출  

---

# ✅ **정리: 전체 패키지 설치 명령어**
📌 **이제 `requirements.txt` 파일을 생성해서 한 번에 설치할 수 있도록 저장하세요.**
```bash
pip freeze > requirements.txt
```
📌 **새로운 환경에서 한 번에 설치할 때**
```bash
pip install -r requirements.txt
```

✅ **이제 가상환경에서 설치된 패키지를 문서화했으니, AI 모델 학습을 진행할 수 있습니다!**  

---

✅ **최종 목표:** 2024년 5월까지 AI 면접 시스템을 완성하고 실전 테스트 진행!

🚀 **배포 방식 결정이 필요하며, Vercel, Railway, Supabase, Cloudflare R2, Hugging Face Spaces를 활용해 무료 배포 가능!**
