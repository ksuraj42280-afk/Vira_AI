from voice import speak, listen
from brain import process


def main():

    speak("Hello Suraj. I am JARVIS. Ready to help you.")

    while True:

        command = listen()

        print("DEBUG:", command)

        if not command:
            continue

        if command.lower() in ["exit", "quit", "goodbye"]:

            speak("Goodbye Suraj.")
            break

        response = process(command)

        speak(response)


if __name__ == "__main__":
    main()