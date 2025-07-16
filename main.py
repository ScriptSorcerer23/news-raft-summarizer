from fastapi import FastAPI
from news_fetcher import fetch_news
from summarizer import summarize_text
from vector_store import embed_and_store, query_similar_docs

app = FastAPI()

@app.get("/summary")
def get_summary(query: str):
    # Step 1: Fetch news articles
    articles = fetch_news(query)
    if not articles:
        return {"error": "No news articles found."}
    
    # Step 2: Store in vector DB
    doc_ids = [f"{query}_{i}" for i in range(len(articles))]
    embed_and_store(articles, doc_ids)

    # Step 3: Retrieve similar articles
    top_docs = query_similar_docs(query)

    # Step 4: Summarize each
    summarized = [summarize_text(doc) for doc in top_docs]

    return {
        "query": query,
        "summaries": summarized
    }
