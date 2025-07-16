

import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma client and collection
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("news_articles")

def embed_and_store(docs: list, ids: list):
    """
    Embed and store documents in the Chroma vector DB.
    """
    embeddings = embedding_model.encode(docs).tolist()
    collection.add(documents=docs, embeddings=embeddings, ids=ids)

def query_similar_docs(query: str, n_results: int = 3):
    """
    Retrieve top-n similar documents from the vector DB.
    """
    query_embedding = embedding_model.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results['documents'][0]
