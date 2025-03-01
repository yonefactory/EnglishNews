import requests
import config
from utils import load_chat_ids

TELEGRAM_URL = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"

def send_message(text):
    chat_ids = load_chat_ids()
    for chat_id in chat_ids:
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        requests.post(TELEGRAM_URL, data=payload)

if __name__ == "__main__":
    send_message("Test message from Telegram bot!")
