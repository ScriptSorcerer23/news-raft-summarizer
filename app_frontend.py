import streamlit as st
from main import get_summary

st.set_page_config(page_title="RAG News Summarizer", layout="wide")

st.title("📰 Real-Time News Summarizer")
st.markdown("Enter a topic below to fetch and summarize real news articles using RAG.")

query = st.text_input("🔍 Topic", placeholder="e.g. Artificial Intelligence")

if st.button("Summarize"):
    with st.spinner("Fetching and summarizing..."):
        try:
            response = get_summary(query)
            summaries = response.get("summaries", [])
            
            if summaries:
                st.success(f"Top Summaries for **{query}**")
                for i, summary in enumerate(summaries, 1):
                    st.markdown(f"**{i}.** {summary}")
            else:
                st.warning("No summaries found.")
        except Exception as e:
            st.error(f"Error: {e}")
