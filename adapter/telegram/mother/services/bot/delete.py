from . import database



async def delete_bot_by_id(botid):
    for bot in database:
        if bot['bot_id'] == botid:
            database.remove(bot)
            return True
    return False
    