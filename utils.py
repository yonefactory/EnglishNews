def load_chat_ids(file_path="data/chat_ids.txt"):
    """텔레그램 메시지를 보낼 chat_id 목록을 불러온다."""
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        return []

def save_chat_ids(chat_ids, file_path="data/chat_ids.txt"):
    """chat_id 목록을 저장한다."""
    with open(file_path, "w") as f:
        f.writelines([chat_id + "\n" for chat_id in chat_ids])
