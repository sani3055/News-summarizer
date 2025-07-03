from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    # Truncate long inputs
    max_input = 1024
    if len(text) > max_input:
        text = text[:max_input]

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
