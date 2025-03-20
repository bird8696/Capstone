import speech_recognition as sr

print("🎙️ 사용 가능한 마이크 장치 확인 중...")
mic_list = sr.Microphone.list_microphone_names()

if not mic_list:
    print("❌ 마이크를 찾을 수 없습니다. 마이크가 연결되었는지 확인하세요!")
else:
    for idx, mic in enumerate(mic_list):
        print(f"🎤 [{idx}] {mic}")
