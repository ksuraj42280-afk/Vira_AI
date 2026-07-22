# memory.py

import json
import os

MEMORY_FILE = "data/memory.json"


def load_memory():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as file:
            json.dump({}, file)

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(key, value):

    memory = load_memory()

    memory[key] = value

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def get_memory(key):

    memory = load_memory()

    return memory.get(key)