
# summarizer.py

from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str, max_length: int = 130, min_length: int = 30):
    if not text or len(text.strip()) < 30:
        return "Text too short to summarize."

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
