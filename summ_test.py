import scraper_news as scraper
from scraper_news import extract_article_text
from summarizer import summarize_text


print("Using scraper from:", scraper.__file__)

url = "https://www.bbc.com/news/articles/cpvjjd7xw8go"
text = extract_article_text(url)
print("Original:", text[:200], "...\n")
print("Summary:", summarize_text(text))

