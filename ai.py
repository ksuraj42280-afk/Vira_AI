# ai.py

import ollama
from memory import save_memory, get_memory
from jarvis_conversation import add, get


# -------------------------
# Main AI Chat
# -------------------------
def ask_ai(prompt):

    text = prompt.lower().strip()

    print("AI RECEIVED:", text)

    # -------------------------
    # Save User Name
    # -------------------------
    if "my name is" in text:

        name = prompt.replace("My name is", "").replace("my name is", "").strip()

        save_memory("name", name)

        return f"Okay, I will remember that your name is {name}."

    # -------------------------
    # Recall User Name
    # -------------------------
    elif (
        "what is my name" in text
        or "what's my name" in text
        or "whats my name" in text
        or "tell me my name" in text
        or "do you know my name" in text
    ):

        name = get_memory("name")

        if name:
            return f"Your name is {name}"
        else:
            return "I don't know your name yet."

    # -------------------------
    # Ollama Chat
    # -------------------------
    try:

        add("user", prompt)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are JARVIS, a helpful personal AI assistant. "
                    "Your creator is Suraj. "
                    "Keep your answers short, clear and friendly."
                ),
            }
        ]

        messages.extend(get())

        response = ollama.chat(
            model="llama3.2",
            messages=messages,
        )

        reply = response["message"]["content"]

        add("assistant", reply)

        return reply

    except Exception as e:

        return f"JARVIS AI Error: {e}"


# -------------------------
# Summarize Web Results
# -------------------------
def summarize_web(query, web_text):

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are JARVIS. "
                        "Read the web search results and answer the user's question "
                        "in simple English. "
                        "Summarize the information in 4-5 sentences. "
                        "Do not copy the search results exactly."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"User Question:\n{query}\n\n"
                        f"Web Search Results:\n{web_text}"
                    ),
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:

        return f"Summary Error: {e}"


# -------------------------
# Hybrid AI
# Decide whether Internet is needed
# -------------------------
def needs_internet(prompt):

    prompt = prompt.lower().strip()

    keywords = [
        "latest",
        "today",
        "news",
        "current",
        "recent",
        "live",
        "weather",
        "temperature",
        "forecast",
        "score",
        "match",
        "ipl",
        "cricket",
        "football",
        "stock",
        "share price",
        "bitcoin",
        "crypto",
        "gold price",
        "election",
        "breaking",
    ]

    return any(keyword in prompt for keyword in keywords)