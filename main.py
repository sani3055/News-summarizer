import streamlit as st
from scraper_news import extract_article_text
from summarizer import summarize_text

# Initialize session state
if 'text' not in st.session_state:
    st.session_state.text = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""

def fetch_article():
    st.session_state.text = extract_article_text(st.session_state.url)

def generate_summary():
    st.session_state.summary = summarize_text(st.session_state.text)

st.set_page_config(page_title="AI News Summarizer", layout="centered")
st.title("AI News Summarizer")

# Input section
mode = st.radio("Choose input:", ["URL", "Text"])
if mode == "URL":
    st.text_input("Article URL:", key="url", on_change=lambda: None)
    st.button("Fetch Article", on_click=fetch_article)
else:
    st.text_area("Paste article text here:", key="text")

# Display article
if st.session_state.text:
    st.subheader("Original (preview)")
    st.write(st.session_state.text[:1000] + "...")
    st.button("Summarize", on_click=generate_summary)

# Display summary
if st.session_state.summary:
    st.subheader("Summary")
    st.success(st.session_state.summary)
