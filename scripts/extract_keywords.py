import openai
import json
import os
from datetime import datetime
from config import OPENAI_API_KEY

KEYWORDS_DATA_PATH = "data/keywords.json"

# OpenAI 클라이언트 인스턴스 생성
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def save_keywords_data(keywords):
    """추출된 키워드를 JSON 파일에 저장"""
    data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "keywords": keywords
    }
    with open(KEYWORDS_DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_keywords_data():
    """저장된 키워드를 불러옴 (오늘 날짜와 일치하면 사용)"""
    if not os.path.exists(KEYWORDS_DATA_PATH):
        return None

    with open(KEYWORDS_DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    if data.get("date") == datetime.now().strftime("%Y-%m-%d"):
        return data["keywords"]
    return None

def extract_keywords(text, model="gpt-3.5-turbo"):
    """최신 OpenAI API 사용하여 키워드 추출"""
    
    saved_keywords = load_keywords_data()
    if saved_keywords:
        return saved_keywords  # 기존 데이터 사용

    prompt = f"Extract 5 essential English business-related keywords, phrases, or idioms from the following summary:\n\n{text}\n\nProvide meanings in Korean."

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a professional English teacher."},
            {"role": "user", "content": prompt}
        ]
    )

    keywords = response.choices[0].message.content.strip().split("\n")

    save_keywords_data(keywords)
    return keywords

if __name__ == "__main__":
    input_text = "The rift between Ukrainian leader Zelensky and American elites has caused uncertainty."
    print(extract_keywords(input_text))
