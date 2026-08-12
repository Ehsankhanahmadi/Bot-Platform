from . import database



async def get_one_user(user):
    for i in database:
        if i["telegram_id"] == user.id:
            print("user already exists")
            return "verified"
    print("user not found")
    return "not verified"