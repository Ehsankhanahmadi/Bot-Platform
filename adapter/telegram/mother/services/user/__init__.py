import os
from dotenv import load_dotenv

ADAPTER_NAME = os.getenv("ADAPTER_NAME")

load_dotenv()

database = [
    {
        "telegram_id": 62470736279,
        "user_name": "Ehsan_web884",
        "is_bot": False,
        "adapter_name": ADAPTER_NAME
    }
]

from .verify import verify_user
from .get import get_one_user