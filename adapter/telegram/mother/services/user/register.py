# import httpx
# import os

# from dotenv import load_dotenv

# load_dotenv()

# API_URL = os.getenv("CORE_API_URL")
# API_TOKEN = os.getenv("ADAPTER_TOKEN")
# ADAPTER_NAME = os.getenv("ADAPTER_NAME")


async def register_user(user):
    payload = {
        "telegram_id": user.id,
        "username": user.username,
        # "first_name": user.first_name,
        # "last_name": user.last_name,
        # "language_code": user.language_code,
        "is_bot": user.is_bot,
        # "adapter_name": ADAPTER_NAME,
    }
    print(payload)
    # async with httpx.AsyncClient(timeout=5) as client:
    #     response = await client.post(f"{API_URL}/users/",json=payload)

        # return response