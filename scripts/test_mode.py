import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
from generate_messages import create_message
from send_telegram import send_message

if __name__ == "__main__":
    test_message = create_message()
    send_message("[TEST MODE] " + test_message)
