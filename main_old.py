import os
import subprocess
import webbrowser
import pyttsx3

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role":"system","content":"You are Jarvis, an intelligent AI assistant."},
                {"role":"user","content":prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)

def open_app(name):

    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "explorer": "explorer"
    }

    if name in apps:
        subprocess.Popen(apps[name])
        speak(f"Opening {name}")
    else:
        speak("Application not found.")

def search_google(query):

    url = "https://www.google.com/search?q=" + query.replace(" ","+")
    webbrowser.open(url)
    speak("Searching Google.")

def open_youtube():

    webbrowser.open("https://youtube.com")
    speak("Opening YouTube.")

def open_chatgpt():

    webbrowser.open("https://chat.openai.com")
    speak("Opening ChatGPT.")

def help_menu():

    print("""
Commands

open chrome
open notepad
open calculator
open paint
open cmd
open explorer
youtube
chatgpt
search <anything>
exit

Anything else will be answered using DeepSeek AI.
""")

def main():

    speak("Hello Sir. I am Jarvis Sir,Your personal AI. How can i assist you ?.")

    help_menu()

    while True:

        command = input("You : ").lower().strip()

        if command == "exit":
            speak("Goodbye.")
            break

        elif command.startswith("open "):
            app = command.replace("open ","")
            open_app(app)

        elif command.startswith("search "):
            search_google(command.replace("search ",""))

        elif command == "youtube":
            open_youtube()

        elif command == "chatgpt":
            open_chatgpt()

        else:
            answer = ask_ai(command)
            speak(answer)

if __name__ == "__main__":
    main()