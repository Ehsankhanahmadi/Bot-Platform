from aiogram.types import Message
from aiogram import F

from . import router



@router.message(F.text == "⚙️ تنظیمات بات")
async def handler_config_bots(message:Message):
    await message.answer("شما روی دکمه تنظیمات بات کلیک کردید")