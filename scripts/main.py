import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
import datetime
from generate_messages import create_message
from send_telegram import send_message

def determine_messages_to_send():
    """현재 시각을 기준으로 어떤 메시지를 보낼지 결정"""
    now = datetime.datetime.now().hour
    messages = []

    if now >= 7:
        messages.append(create_message())  # 오전 7시 뉴스 요약

    return messages

if __name__ == "__main__":
    messages = determine_messages_to_send()
    for msg in messages:
        send_message(msg)
