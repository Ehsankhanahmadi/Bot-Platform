from . import database
from aiogram import Bot
from aiogram.exceptions import TelegramUnauthorizedError



# CREATE
async def create_bot(token: str, userid: int, status: bool = True):
    bot = None 
    try: 
        bot = Bot(token) 
        bot_info = await bot.get_me() 
        for bot_item in database: 
            if bot_item["bot_id"] == bot_info.id: 
                return {"success": False, "reason": "already_exists"} 
            bot_new = { 
                "token": token,
                "bot_username": f"@{bot_info.username}", 
                "bot_id": bot_info.id, 
                "user_id": userid, 
                "active": status, 
                "assignment": None, 
            } 
            database.append(bot_new) 
            print(bot_new)
            print(database)
            return {"success": True, "reason": "created", "bot": bot_info, "data": bot_new} 
    except TelegramUnauthorizedError: 
        print("[BOT] Invalid Telegram token ❌") 
        return {"success": False, "reason": "invalid_token"} 
    except Exception as e: 
        print(f"[BOT] Telegram connection error: {e}") 
        return {"success": False, "reason": "telegram_error", "error": e} 
    finally:
        if bot is not None: 
            await bot.session.close()


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