from . import database



async def create_bot(botmain,token,userid,status:None):
    bot_new = {
        "token": f'{token}',
        "bot_username": f'@{botmain.username}',
        "bot_id": botmain.id,
        "user_id": userid,
        "active": status | True
    }
    for bot in database:
        if bot['bot_id'] == botmain.id:
            print("bot already exists")
            return False
    database.append(bot_new)
    print(bot_new)
    print(database)
    return True