from fastapi import HTTPException
from aiogram.types import Update

from runtime.registry import get_bot



async def process_child_update(bot_id: int,data: dict,):
    bot_data = await get_bot(bot_id)
    if not bot_data:
        raise HTTPException(status_code=404,detail="Bot not found in this runtime",)
    bot = bot_data["bot"]
    dp = bot_data["dispatcher"]
    update = Update.model_validate(data,context={"bot": bot,},)
    await dp.feed_update(bot,update)