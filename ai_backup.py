# ai_backup.py

import ollama


def ask_ai(prompt):

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": "You are JARVIS, a helpful personal AI assistant created by Suraj."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"JARVIS AI Error: {e}"