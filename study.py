from dotenv import load_dotenv
load_dotenv()

import requests
from google import genai

client = genai.Client()

def search_wikipedia(query: str) -> str:
    """Searches Wikipedia and returns a short summary of the top matching article."""
    # Step A: find the best matching article title
    search = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "opensearch",
            "search": query,
            "limit": 1,
            "format": "json",
        }
    ).json()

    titles = search[1]
    if not titles:
        return f"No Wikipedia article found for '{query}'."

    title = titles[0]

    # Step B: get a short summary of that article
    summary = requests.get(
        f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    ).json()

    return summary.get("extract", "No summary available.")

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={"tools": [search_wikipedia]}
)

response = chat.send_message("Who was Ada Lovelace and why is she famous?")
print("Gemini:", response.text)

