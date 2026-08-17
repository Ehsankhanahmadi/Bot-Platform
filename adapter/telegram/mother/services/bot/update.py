from . import database, delete_bot_by_id, create_bot



async def update_bot(botmain,token,userid,status:None):
    for bot in database:
        if bot['bot_id'] == botmain.id:
            await delete_bot_by_id(botmain.id)
            await create_bot(botmain,token,userid,status)
            return True
    return False