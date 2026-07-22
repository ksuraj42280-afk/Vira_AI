from voice import speak, listen

speak("Hello Suraj. I am Jarvis.")

while True:
    command = listen()

    if command == "":
        continue

    if "exit" in command:
        speak("Goodbye.")
        break

    speak("You said " + command)