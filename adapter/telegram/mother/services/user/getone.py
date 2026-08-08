from . import ADAPTER_NAME,database



async def get_one_user(user):
    user_data = {
        "telegram_id": user.id,
        "user_name": user.username,
        "is_bot": user.is_bot,
        "adapter_name": ADAPTER_NAME,
    }
    if user_data in database:
        print("user already exists")
        return "verified"
    else:
        print("user not found")
        return "not verified"