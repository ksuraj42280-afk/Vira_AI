# system_handler.py

from system import (
    get_time,
    get_date,
    get_battery,
    get_cpu,
    get_ram,
    get_pc_name,
    get_os,
)


def handle(command):

    if "time" in command:
        return f"Current time is {get_time()}"

    elif "date" in command:
        return f"Today is {get_date()}"

    elif "battery" in command:
        return f"Battery percentage is {get_battery()}"

    elif "cpu" in command:
        return f"CPU usage is {get_cpu()}"

    elif "ram" in command or "memory" in command:
        return f"RAM usage is {get_ram()}"

    elif "computer name" in command:
        return f"Computer name is {get_pc_name()}"

    elif "operating system" in command or "windows version" in command:
        return f"You are using {get_os()}"

    return None