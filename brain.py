# brain.py

from calculator import calculate

from ai import (
    ask_ai,
    summarize_web,
)

from internet import get_web_text

from logger import log

from decision import decide

from system_handler import handle as system_handler

from automation_handler import handle as automation_handler

from internet_handler import handle as internet_handler

from ai_handler import handle as ai_handler

def process(command):

    command = command.lower().strip()

    # Log User Command
    log("USER", command)

    # Decision Engine
    task = decide(command)

    print("TASK:", task)


    # -------------------------
    # Calculator
    # -------------------------
    if task == "calculator":

        answer = calculate(command)

        if answer is not None:
            reply = f"The answer is {answer}"
        else:
            reply = "I could not calculate that."


    # -------------------------
    # System
    # -------------------------
    elif task == "system":

        reply = system_handler(command)


    # -------------------------
    # Automation
    # -------------------------
    elif task == "automation":

        reply = automation_handler(command)

    # -------------------------
    # Internet
    # -------------------------
    elif task == "internet":

        reply = internet_handler(command)


    # -------------------------
    # AI
    # -------------------------
    else:

        reply = ask_ai(command)


    # Log Response
    log("JARVIS", reply)

    return reply