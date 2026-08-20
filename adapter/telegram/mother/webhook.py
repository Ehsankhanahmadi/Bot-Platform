import os
from aiogram.types import Update

from .bot import bot
from .dispatcher import dp

from child.runtime.manager import shutdown_bots

WEBHOOK_URL = os.getenv("WEBHOOK_URL")



async def process_update(data: dict):
    update = Update.model_validate(data,context={"bot": bot})
    await dp.feed_update(bot,update)


async def set_webhook():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=f"{WEBHOOK_URL}/telegram/webhook", allowed_updates=dp.resolve_used_update_types())
    print("Webhook Registered ✅")


async def shutdown():
    await bot.session.close()
    await shutdown_bots()