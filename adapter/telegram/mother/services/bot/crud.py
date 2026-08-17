from . import database


# CREATE
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


# READ 
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


# UPDATE
async def update_bot(botmain,token,userid,status:None):
    for bot in database:
        if bot['bot_id'] == botmain.id:
            await delete_bot_by_id(botmain.id)
            await create_bot(botmain,token,userid,status)
            return True
    return False


# DELETE
async def delete_bot_by_id(botid):
    for bot in database:
        if bot['bot_id'] == botid:
            database.remove(bot)
            return True
    return False