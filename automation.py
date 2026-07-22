from PIL import ImageGrab
from datetime import datetime
import subprocess
import webbrowser
import os
import ctypes


# ==========================================
# Installed Applications
# ==========================================

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "explorer": "explorer",
}


# ==========================================
# Open Application
# ==========================================

def open_application(app_name):

    app_name = app_name.lower().strip()

    if app_name in APPS:
        subprocess.Popen(APPS[app_name])
        return f"Opening {app_name}"

    return "Application not found."


# ==========================================
# Google Search
# ==========================================

def google_search(query):

    webbrowser.open(
        "https://www.google.com/search?q=" +
        query.replace(" ", "+")
    )

    return "Searching Google."


# ==========================================
# YouTube
# ==========================================

def open_youtube():

    webbrowser.open("https://www.youtube.com")

    return "Opening YouTube."


def youtube_search(query):

    webbrowser.open(
        "https://www.youtube.com/results?search_query=" +
        query.replace(" ", "+")
    )

    return "Searching YouTube."


# ==========================================
# Screenshot
# ==========================================

def take_screenshot():

    folder = "Screenshots"

    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

    path = os.path.join(folder, filename)

    image = ImageGrab.grab()

    image.save(path)

    return f"Screenshot saved at {path}"


# ==========================================
# Lock Computer
# ==========================================

def lock_pc():

    ctypes.windll.user32.LockWorkStation()

    return "Locking computer."


# ==========================================
# Shutdown
# ==========================================

def shutdown():

    os.system("shutdown /s /t 10")

    return "Shutdown will start in 10 seconds."


# ==========================================
# Restart
# ==========================================

def restart():

    os.system("shutdown /r /t 10")

    return "Restart will start in 10 seconds."