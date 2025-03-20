import openai
import os
from dotenv import load_dotenv

# `.env` 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ API 키가 설정되지 않았습니다! `.env` 파일을 확인하세요.")

# 최신 OpenAI 라이브러리 방식
openai.api_key = OPENAI_API_KEY
client = openai.Client()

# 면접 질문 생성 함수
def generate_interview_question(job_role):
    job_categories = {
        "프론트엔드 개발자": "React, TypeScript, JavaScript, UI/UX 관련 질문",
        "백엔드 개발자": "FastAPI, SQL, Python, 서버 구조 관련 질문",
        "AI 엔지니어": "딥러닝, 모델 학습, NLP 관련 기술 면접 질문"
    }

    prompt = f"{job_categories.get(job_role, '일반적인')}을 주제로 한 기술 면접 질문 하나만 생성해주세요."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 면접관입니다."},
            {"role": "user", "content": prompt}
        ]
    )

    question = response.choices[0].message.content
    return question

# 테스트 실행
if __name__ == "__main__":
    job_role = input("면접 질문을 생성할 직군을 입력하세요 (프론트엔드 개발자 / 백엔드 개발자 / AI 엔지니어): ").strip()
    question = generate_interview_question(job_role)
    print(f"🔹 생성된 질문: {question}")
