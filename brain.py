# brain.py

from calculator import calculate

from ai import (
    ask_ai,
    summarize_web,
    needs_internet,

)

from internet import get_web_text

from logger import log

from automation import (
    open_application,
    google_search,
    open_youtube,
    youtube_search,
    take_screenshot,
)

from system import (
    get_time,
    get_date,
    get_battery,
    get_cpu,
    get_ram,
    get_pc_name,
    get_os,
)


def process(command):

    command = command.lower().strip()

    # Log User Command
    log("USER", command)

    # -------------------------
    # Calculator
    # -------------------------
    answer = calculate(command)

    if answer is not None:
        reply = f"The answer is {answer}"

    # -------------------------
    # Time
    # -------------------------
    elif "time" in command:
        reply = f"Current time is {get_time()}"

    # -------------------------
    # Date
    # -------------------------
    elif "date" in command:
        reply = f"Today is {get_date()}"

    # -------------------------
    # Battery
    # -------------------------
    elif "battery" in command:
        reply = f"Battery percentage is {get_battery()}"

    # -------------------------
    # CPU
    # -------------------------
    elif "cpu" in command:
        reply = f"CPU usage is {get_cpu()}"

    # -------------------------
    # RAM
    # -------------------------
    elif "ram" in command or "memory" in command:
        reply = f"RAM usage is {get_ram()}"

    # -------------------------
    # Computer Name
    # -------------------------
    elif "computer name" in command:
        reply = f"Computer name is {get_pc_name()}"

    # -------------------------
    # Operating System
    # -------------------------
    elif "operating system" in command or "windows version" in command:
        reply = f"You are using {get_os()}"

    # -------------------------
    # Open Application
    # -------------------------
    elif command.startswith("open "):

        app = command.replace("open ", "").strip()

        reply = open_application(app)

    # -------------------------
    # Search YouTube
    # -------------------------
    elif command.startswith("search youtube for "):

        query = command.replace("search youtube for ", "").strip()

        reply = youtube_search(query)

    # -------------------------
    # Google Search
    # -------------------------
    elif command.startswith("search "):

        query = command.replace("search ", "").strip()

        reply = google_search(query)

    # -------------------------
    # Internet Search + AI Summary
    # -------------------------
    elif command.startswith("internet "):

        query = command.replace("internet ", "").strip()

        web_results = get_web_text(query)

        reply = summarize_web(query, web_results)

    # -------------------------
    # Open YouTube
    # -------------------------
    elif command == "youtube" or command == "open youtube":

        reply = open_youtube()

    # -------------------------
    # Screenshot
    # -------------------------
    elif "screenshot" in command:

        reply = take_screenshot()

    # -------------------------
    # AI / Hybrid AI
    # -------------------------
    else:

        if needs_internet(command):

            web_results = get_web_text(command)

            reply = summarize_web(command, web_results)

        else:

            reply = ask_ai(command)
            # Log Jarvis Response
            log("JARVIS", reply)

            return reply