import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
import requests
from bs4 import BeautifulSoup

BBC_URL = "https://www.bbc.com/news"

def get_top_bbc_news():
    """BBC 뉴스 홈페이지에서 가장 중요한 기사를 가져온다."""
    response = requests.get(BBC_URL)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    top_article = soup.select_one(".gs-c-promo-heading")
    if not top_article:
        return None

    title = top_article.text.strip()
    link = BBC_URL + top_article["href"]

    article_response = requests.get(link)
    article_soup = BeautifulSoup(article_response.text, "html.parser")

    paragraphs = article_soup.select("article p")
    content = " ".join([p.text.strip() for p in paragraphs[:5]])  # 첫 5개 문단 요약

    return {"title": title, "content": content, "url": link}

if __name__ == "__main__":
    news = get_top_bbc_news()
    if news:
        print(f"Title: {news['title']}\nContent: {news['content']}\nURL: {news['url']}")
