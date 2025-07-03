# scraper.py
from newspaper import Article

def extract_article_text(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text

if __name__ == "__main__":
    # quick self-test
    test_url = "https://www.bbc.com/news/articles/cpvjjd7xw8go"
    text = extract_article_text(test_url)
    print("Preview:", text[:200])
