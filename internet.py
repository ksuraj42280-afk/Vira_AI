# internet.py

from ddgs import DDGS


def search(query, max_results=5):
    """
    Search the internet and return formatted results.
    """

    try:

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))

        if not results:
            return "Sorry, I couldn't find anything."

        answer = ""

        for i, result in enumerate(results, start=1):

            title = result.get("title", "No Title")
            body = result.get("body", "")
            url = result.get("href", "")

            answer += f"{i}. {title}\n"
            answer += f"{body}\n"

            if url:
                answer += f"{url}\n"

            answer += "\n"

        return answer

    except Exception as e:
        return f"Internet Error: {e}"


def get_web_text(query):
    """
    Returns clean web text for AI summarization.
    """
    return search(query)