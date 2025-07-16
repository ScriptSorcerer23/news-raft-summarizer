
# news_fetcher.py

import requests

gnews_api_key = "95c5a1b86451aa76c69a98593bda0721"

def fetch_news(query: str, max_results: int = 5):
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max={max_results}&token={gnews_api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [article.get("description") or article.get("content") for article in articles if article.get("description")]
