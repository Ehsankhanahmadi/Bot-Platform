from . import get_bot_by_id, database



async def status_change(botid, status):
    bot = await get_bot_by_id(botid)
    if bot:
        if bot in database:
            bot["active"] = status
            return True
        return False