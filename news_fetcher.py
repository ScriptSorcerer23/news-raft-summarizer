import os
import requests
from dotenv import load_dotenv

load_dotenv()  

gnews_api_key = os.getenv("GNEWS_API_KEY")


def fetch_news(query: str, max_results: int = 5):
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max={max_results}&token={gnews_api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [article.get("description") or article.get("content") for article in articles if article.get("description")]
