from . import database



async def create_bot(bot_username,token,userid):
    bot = {
        "token": f'{token}',
        "bot_username": f'@{bot_username}',
        "user_id": userid,
        "active": True
    }
    for bot in database:
        if bot['bot_username'] == bot_username:
            print("bot already exists")
            return False
    database.append(bot)
    print(bot)
    print(database)
    return True