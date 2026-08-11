from . import database



async def create_bot(bot_username,token,userid):
    bot = {
        "token": f'{token}',
        "bot_username": f'@{bot_username}',
        "user_id": userid,
        "active": True
    }
    if bot in database:
        print("bot already exists")
        return False
    else:
        database.append(bot)
        print(bot)
        print(database)
        return True