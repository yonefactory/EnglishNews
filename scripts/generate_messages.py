import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config

from fetch_news import get_top_bbc_news
from extract_keywords import extract_keywords

def create_message():
    """CNN 뉴스에서 데이터를 가져와 학습 메시지를 생성"""
    news = get_top_cnn_news()
    if not news:
        return "오늘의 뉴스 기사를 가져오지 못했습니다."

    keywords = extract_keywords(news["content"]).split("\n")  # 키워드 리스트 변환
    keyword_list = "\n".join([f"{i+1}. {kw}" for i, kw in enumerate(keywords[:5])])

    message = f"""📚 ****오늘의 영어 학습****

📰 ****오늘의 뉴스 헤드라인:****     
  {news['title']}  
📌 {news['content']}  
🔗 {news['url']}  

🔎 ****오늘의 키워드****  
{keyword_list}
"""

    return message

if __name__ == "__main__":
    print(create_message())
