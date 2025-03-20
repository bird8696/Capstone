import openai
import os
import time
import wave
import pyaudio
import speech_recognition as sr
from dotenv import load_dotenv

# ✅ `.env` 파일 로드
load_dotenv()

# ✅ 환경 변수에서 API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ API 키가 설정되지 않았습니다! `.env` 파일을 확인하세요.")

# ✅ OpenAI API 클라이언트 생성
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# ✅ 음성 저장 폴더 설정
RECORDING_DIR = "E:/Capstone2/Capstone/ai_model/recordings"
os.makedirs(RECORDING_DIR, exist_ok=True)

# ✅ 면접 질문 생성 함수
def generate_interview_question():
    prompt = "FastAPI, SQL, Python, 서버 구조 관련 기술 면접 질문 하나만 생성해주세요."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 면접관입니다."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# ✅ 음성 녹음 및 STT 변환 함수
def record_audio(question_num):
    """
    1. 최대 60초 동안 녹음
    2. 10초 이상 말이 없으면 자동 종료
    3. 녹음된 음성을 파일로 저장
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 60  # 최대 녹음 시간
    SILENCE_LIMIT = 10  # 10초 이상 무음이면 종료

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    start_time = time.time()
    silence_start = None

    print(f"🎙️ 답변을 말해주세요 (최대 {RECORD_SECONDS}초)...")

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        elapsed_time = time.time() - start_time

        # 🔍 **무음 감지 (10초 동안 아무 소리도 없으면 종료)**
        audio_energy = sum(abs(int.from_bytes(data[i:i+2], 'little', signed=True))
                           for i in range(0, len(data), 2)) / CHUNK
        if audio_energy < 500:  # 기본 임계값보다 작은 경우 무음으로 판단
            if silence_start is None:
                silence_start = time.time()
            elif time.time() - silence_start >= SILENCE_LIMIT:
                print("⏭️ 10초 동안 입력이 없어 다음 질문으로 넘어갑니다.")
                break
        else:
            silence_start = None  # 다시 말하면 무음 타이머 리셋

        if elapsed_time >= RECORD_SECONDS:
            print("⏹️ 최대 응답 시간(60초) 도달. 녹음을 종료합니다.")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    # 🎤 **녹음된 오디오 저장**
    audio_path = os.path.join(RECORDING_DIR, f"answer_{question_num}.wav")
    wf = wave.open(audio_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"💾 녹음 파일 저장됨: {audio_path}")
    return audio_path

# ✅ 음성 인식 (STT) 변환 함수
def recognize_speech(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # 전체 오디오 읽기

    try:
        response_text = recognizer.recognize_google(audio, language="ko-KR")
        return response_text
    except sr.UnknownValueError:
        return "음성을 인식하지 못했습니다."
    except sr.RequestError:
        return "STT 서비스 오류가 발생했습니다."

# ✅ 면접 실행 함수
def start_interview():
    print("\n🛠️ [백엔드 개발자 면접 시작]\n")

    for i in range(3):  # 3개 질문 예제
        question = generate_interview_question()
        print(f"\n🔹 질문 {i+1}: {question}")

        audio_file = record_audio(i + 1)
        answer = recognize_speech(audio_file)

        print(f"🗣️ 응답: {answer}")

# ✅ 실행
if __name__ == "__main__":
    start_interview()
