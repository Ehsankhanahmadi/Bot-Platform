import os

from .worker import create_bot_worker
from .registry import get_bot, update_status, remove_bot

WEBHOOK_URL = os.getenv("WEBHOOK_URL")



async def start_bot(token:str,bot_id:int):
    bot = await create_bot_worker(token,bot_id)
    dp = bot["dispatcher"]
    await bot["bot"].delete_webhook(drop_pending_updates=True)
    await bot["bot"].set_webhook(url=f"{WEBHOOK_URL}/telegram/webhook/{bot_id}", allowed_updates=dp.resolve_used_update_types())
    return True


async def stop_bot(bot_id:int):
    bot_data = get_bot(bot_id)
    if not bot_data:
        return False
    bot = bot_data["bot"]
    await bot.delete_webhook()
    update_status(bot_id,"stopped")
    return True


async def restart_bot(token:str,bot_id:int):
    await stop_bot(bot_id)
    remove_bot(bot_id)
    await start_bot(token,bot_id)
    return True