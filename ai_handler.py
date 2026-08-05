# ai_handler.py

from ai import ask_ai


def handle(command):
    """
    Handles all local AI queries.
    """

    command = command.strip()

    try:

        return ask_ai(command)

    except Exception as e:

        return f"AI Handler Error: {e}"