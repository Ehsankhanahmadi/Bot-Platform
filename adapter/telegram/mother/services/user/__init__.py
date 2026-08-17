import os
from dotenv import load_dotenv

ADAPTER_NAME = os.getenv("ADAPTER_NAME")

load_dotenv()

database = [
    {
        "telegram_id": 6247073627,
        "user_name": "Ehsan_web884",
        "is_bot": False,
        "adapter_name": ADAPTER_NAME,
        "phone_number": '989909572056' ,
    }
]

from .verify import verify_user
from .crud import get_one_user