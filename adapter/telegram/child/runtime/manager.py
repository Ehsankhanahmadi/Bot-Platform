import os

from .worker import create_bot_worker
from .registry import get_bot, get_all_bots, remove_bot
# from .ownership import release_bot

WEBHOOK_URL = os.getenv("WEBHOOK_URL")



async def start_bot(bot_config: dict):
    token = bot_config["token"]
    bot_id = bot_config["bot_id"]
    bot_data = await create_bot_worker(token,bot_id,bot_config,)
    if not bot_data:
        return False
    bot = bot_data["bot"]
    dp = bot_data["dispatcher"]
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=f"{WEBHOOK_URL}/telegram/webhook/{bot_id}", allowed_updates=dp.resolve_used_update_types())
    print("Webhook Registered ✅")
    return True


async def stop_bot(bot_id: int):
    bot_data = await get_bot(bot_id)
    if not bot_data:
        return False
    bot = bot_data["bot"]
    try:
        await bot.delete_webhook()
    except Exception:
        pass

    try:
        await bot.session.close()
    except Exception:
        pass
    # await release_bot(bot_id)
    await remove_bot(bot_id)
    return True


async def shutdown_bots():
    bots = await get_all_bots()
    for bot_id, bot_data in list(bots.items()):
        bot = bot_data["bot"]
        try:
            await bot.delete_webhook()
        except Exception:
            pass

        try:
            await bot.session.close()
        except Exception:
            pass
        # await release_bot(bot_id)
        await remove_bot(bot_id)