# internet_handler.py

from internet import get_web_text
from ai import summarize_web


def handle(command):

    command = command.strip()

    web_results = get_web_text(command)

    return summarize_web(command, web_results)