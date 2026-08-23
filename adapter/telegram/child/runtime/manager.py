import os

from .worker import create_bot_worker
from .registry import get_bot, get_all_bots, update_status, remove_bot

WEBHOOK_URL = os.getenv("WEBHOOK_URL_CHILD")



async def start_bot(bot_config:dict):
    token = bot_config["token"]
    bot_id = bot_config["bot_id"]
    bot = await create_bot_worker(token,bot_id,bot_config)
    dp = bot["dispatcher"]
    await bot["bot"].delete_webhook(drop_pending_updates=True)
    await bot["bot"].set_webhook(url=f"{WEBHOOK_URL}/telegram/webhook/{bot_id}", allowed_updates=dp.resolve_used_update_types())
    # await bot["bot"].set_webhook(url=f"{WEBHOOK_URL}/telegram/webhook/{bot_id}", allowed_updates=[])
    print("Webhook Registered ✅")
    return True


async def stop_bot(bot_id:int):
    bot_data = get_bot(bot_id)
    if not bot_data:
        return False
    bot = bot_data["bot"]
    await bot.delete_webhook()
    update_status(bot_id,"stopped")
    return True


async def restart_bot(bot_config: dict):
    bot_id = bot_config["bot_id"]
    await stop_bot(bot_id)
    remove_bot(bot_id)
    await start_bot(bot_config)
    return True


async def shutdown_bots():
    bots = get_all_bots()
    for bot_id, bot_data in list(bots.items()):
        bot = bot_data["bot"]
        try:
            await bot.delete_webhook()
        except Exception:
            pass
        await bot.session.close()