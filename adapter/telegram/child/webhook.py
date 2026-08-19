from fastapi import Request, HTTPException
from aiogram.types import Update

from .runtime.registry import get_bot, registry



async def process_update(bot_id:int,data:dict):
    bot_data = get_bot(bot_id)
    if not bot_data:
        raise HTTPException(status_code=404,detail="Bot not found")
    bot = bot_data["bot"]
    dp = bot_data["dispatcher"]
    update = Update.model_validate(data,context={"bot": bot})
    await dp.feed_update(bot,update)


async def shutdown():
    for bot_id, bot_data in registry.items():
        bot = bot_data["bot"]
        await bot.session.close()