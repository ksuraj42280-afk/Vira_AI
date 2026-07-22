import psutil
import platform
import socket
from datetime import datetime


def get_time():
    """Return current time."""
    return datetime.now().strftime("%I:%M %p")


def get_date():
    """Return current date."""
    return datetime.now().strftime("%d %B %Y")


def get_battery():
    """Return battery percentage."""
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is not available."

    status = "Charging" if battery.power_plugged else "Not Charging"

    return f"{battery.percent}% ({status})"


def get_cpu():
    """Return CPU usage."""
    return f"{psutil.cpu_percent(interval=1)}%"


def get_ram():
    """Return RAM usage."""
    memory = psutil.virtual_memory()

    return (
        f"{memory.percent}% used "
        f"({round(memory.used / (1024**3),2)} GB / "
        f"{round(memory.total / (1024**3),2)} GB)"
    )


def get_pc_name():
    """Return computer name."""
    return socket.gethostname()


def get_os():
    """Return OS details."""
    return f"{platform.system()} {platform.release()}"