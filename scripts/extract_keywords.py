import openai
import config

def extract_keywords(text):
    """ChatGPT를 사용하여 기사에서 중요한 5개의 키워드를 추출"""
    openai.api_key = config.OPENAI_API_KEY
    prompt = f"Extract 5 essential English keywords or idioms from the following news summary:\n\n{text}\n\nProvide meanings in Korean."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    sample_text = "The economy is facing a recession due to supply chain issues."
    keywords = extract_keywords(sample_text)
    print(keywords)
