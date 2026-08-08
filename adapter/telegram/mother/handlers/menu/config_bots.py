from aiogram.types import Message
from aiogram import F

from mother.keyboards import verify_keyboard
from mother.services import get_one_user

from . import router



@router.message(F.text == "⚙️ تنظیمات بات")
async def handler_config_bots(message:Message):
    user = await get_one_user(message.from_user)
    if user != "verified":
        await message.answer("🌚", reply_markup=verify_keyboard)
    else:
        await message.answer("شما روی دکمه تنظیمات بات کلیک کردید")