import speech_recognition as sr
import pyttsx3


def speak(text):
    print("Jarvis:", text)

    try:
        engine = pyttsx3.init()

        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)

        engine.setProperty("rate", 180)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print("Speech Error:", e)


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("🔄 Recognizing...")

            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

        except Exception as e:
            print(e)
            speak("Microphone error.")
            return ""