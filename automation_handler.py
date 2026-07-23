# automation_handler.py

from automation import (
    open_application,
    google_search,
    open_youtube,
    youtube_search,
    take_screenshot,
)


def handle(command):

    command = command.lower().strip()


    # Open Application
    if command.startswith("open "):

        app = command.replace("open ", "").strip()

        return open_application(app)


    # YouTube Search
    elif command.startswith("search youtube for "):

        query = command.replace(
            "search youtube for ",
            ""
        ).strip()

        return youtube_search(query)


    # Google Search
    elif command.startswith("search "):

        query = command.replace(
            "search ",
            ""
        ).strip()

        return google_search(query)


    # Open YouTube
    elif command == "youtube" or command == "open youtube":

        return open_youtube()


    # Screenshot
    elif "screenshot" in command:

        return take_screenshot()


    return "I could not understand the automation command."