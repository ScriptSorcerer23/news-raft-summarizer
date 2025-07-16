# Real-Time News Summarizer using RAFT (Fine-Tuned RAG with FastAPI, Chroma & HuggingFace)

This is a full RAFT project — **Retrieval-Augmented Fine-Tuning** — where a summarization model is fine-tuned on real news data to deliver smarter, personalized summaries using retrieval-augmented generation.

---

## 💡 What It Does

- 🔍 **Fetches live news** from GNews API
- 🧠 **Stores articles as vector embeddings** using SentenceTransformers + ChromaDB
- 🔎 **Retrieves most relevant articles** via semantic search
- ✍️ **Summarizes results** using a **fine-tuned DistilBART model** (on CNN/DailyMail data)
- 🌐 **FastAPI backend** + 🖥️ **Streamlit frontend**

---

## 🔧 Tech Stack

| Layer        | Tool |
|--------------|------|
| Retriever    | `sentence-transformers`, `ChromaDB` |
| Fine-Tuned Generator | `DistilBART` (HuggingFace Transformers) |
| Backend      | `FastAPI` |
| Frontend     | `Streamlit` |
| Vector DB    | `Chroma` (free, local) |
| Trainer      | `HuggingFace Datasets + Transformers` |

---

## 🚀 How to Run Locally


git clone https://github.com/ScriptSorcerer23/news-raft-summarizer.git

cd news-raft-summarizer

 1. Create a .env file with your GNews API key
 
   cp .env.example .env
 
 Then open .env and paste your key:
 GNEWS_API_KEY=your_actual_api_key_here

 2. Install dependencies
 
 pip install -r requirements.txt

 3. Run FastAPI backend
 
 uvicorn main:app --reload

 4. Run Streamlit frontend (in a new terminal/tab)
 
 streamlit run app_frontend.py
