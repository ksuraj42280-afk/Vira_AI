# internet.py

from ddgs import DDGS


def search(query):

    try:

        with DDGS() as ddgs:

            results = list(ddgs.text(query, max_results=3))

        if not results:
            return "Sorry, I couldn't find anything."

        answer = ""

        for i, result in enumerate(results, start=1):

            answer += f"{i}. {result['title']}\n"
            answer += f"{result['body']}\n\n"

        return answer

    except Exception as e:

        return f"Internet Error: {e}"


def get_web_text(query):
    """
    Returns raw web search results.
    """
    return search(query)