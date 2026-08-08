import os
from dotenv import load_dotenv

ADAPTER_NAME = os.getenv("ADAPTER_NAME")

load_dotenv()

database = [
    {
        "telegram_id": 6247073627,
        "user_name": "Ehsan_web884",
        "is_bot": False,
        "adapter_name": ADAPTER_NAME
    }
]



async def verify_user(user):
    user_data = {
        "telegram_id": user.id,
        "user_name": user.username,
        "is_bot": user.is_bot,
        "adapter_name": ADAPTER_NAME,
    }
    if user_data in database:
        print("user already exists")
    else:
        database.append(user_data)
        print(user_data)
        print(database)