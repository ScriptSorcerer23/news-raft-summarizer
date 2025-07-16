from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("Sumama13/raft-summarizer")
model = AutoModelForSeq2SeqLM.from_pretrained("Sumama13/raft-summarizer")


summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text: str, max_length: int = 130, min_length: int = 30):
    if not text or len(text.strip()) < 30:
        return "Text too short to summarize."
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
