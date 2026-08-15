from . import database



async def get_all_bot(userid):
    return [
        i
        for i in database
        if i["user_id"] == userid
    ]

async def get_all_active_bot(userid):
    return [
        bot
        for bot in database
        if bot["user_id"] == userid and bot["active"] is True
    ]

async def get_all_inactive_bot(userid):
    return [
        bot
        for bot in database
        if bot["user_id"] == userid and bot["active"] is False
    ]

async def get_bot_by_id(botid):
    for bot in database:
        if bot["bot_id"] == botid:
            return bot