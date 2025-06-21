from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    if not text.strip():
        return "No readable text found."
    result = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return result[0]['summary_text']