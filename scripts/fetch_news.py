import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
import requests
from bs4 import BeautifulSoup

CNN_URL = "https://edition.cnn.com/world"

def get_top_cnn_news():
    """CNN 국제 뉴스 홈페이지에서 가장 중요한 기사를 가져온다."""
    try:
        response = requests.get(CNN_URL, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"🚨 CNN 뉴스 페이지 로딩 실패: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # 최신 뉴스 기사 찾기
    top_article = soup.find("a", class_="container__link")
    if not top_article or not top_article.get("href"):
        print("🚨 CNN 뉴스 기사를 찾을 수 없습니다.")
        return None

    title = top_article.text.strip()
    link = "https://edition.cnn.com" + top_article["href"]

    # 기사 본문 가져오기
    try:
        article_response = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
        article_response.raise_for_status()
    except requests.RequestException:
        print("🚨 CNN 뉴스 본문 요청 실패")
        return None

    article_soup = BeautifulSoup(article_response.text, "html.parser")
    paragraphs = article_soup.find_all("p")

    content = " ".join([p.text.strip() for p in paragraphs[:5]]) if paragraphs else None

    if not content:
        print("🚨 CNN 뉴스 본문을 찾을 수 없습니다.")
        return None

    return {"title": title, "content": content, "url": link}

if __name__ == "__main__":
    news = get_top_cnn_news()
    if news:
        print(f"Title: {news['title']}\nContent: {news['content']}\nURL: {news['url']}")
