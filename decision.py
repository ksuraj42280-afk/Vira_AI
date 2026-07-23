# decision.py

from ai import needs_internet


def decide(command):

    command = command.lower().strip()

    # Calculator
    if any(op in command for op in ["+", "-", "*", "/", "%"]):
        return "calculator"

    # Time / Date / System
    if any(word in command for word in [
        "time",
        "date",
        "battery",
        "cpu",
        "ram",
        "memory",
        "computer name",
        "operating system",
        "windows version",
    ]):
        return "system"

    # Automation
    if (
        command.startswith("open ")
        or command.startswith("search ")
        or "youtube" in command
        or "screenshot" in command
    ):
        return "automation"

    # Internet
    if needs_internet(command):
        return "internet"

    # AI
    return "ai"