from aiogram.types import Message
from aiogram import F

from . import router



@router.message(F.text == "🤖 ساخت بات")
async def handler_create_bots(message:Message):
    await message.answer("شما روی دکمه ساخت بات کلیک کردید")