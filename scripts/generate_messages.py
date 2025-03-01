import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config

from fetch_news import fetch_valid_news_data
from extract_keywords import extract_keywords

def create_message():
    """CNN 뉴스 데이터를 가져와 학습 메시지를 생성"""
    news_title, news_url, news_content = fetch_valid_news_data()
    if not news_title or news_content == "No Summary Available":
        return "오늘의 뉴스 기사를 가져오지 못했습니다."

    keywords = extract_keywords(news_content)  # ✅ 리스트 그대로 사용

    keyword_list = "\n".join([f"{i+1}. {kw}" for i, kw in enumerate(keywords[:5])])

    message = f"""📚 ****오늘의 영어 학습****

📰 ****오늘의 뉴스 헤드라인:****     
  {news_title}  
📌 {news_content[:200]}...  
🔗 {news_url}  

🔎 ****오늘의 키워드****  
{keyword_list}
"""

    return message

if __name__ == "__main__":
    print(create_message())
