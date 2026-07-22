import speech_recognition as sr
import traceback

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("🎤 Say: Hello Jarvis")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    print("Recognizing...")

    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)

except Exception as e:
    print("FULL ERROR:")
    traceback.print_exc()