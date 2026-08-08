from . import ADAPTER_NAME,database



async def verify_user(user):
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
        database.append(user_data)
        print(user_data)
        print(database)
        return "user added"