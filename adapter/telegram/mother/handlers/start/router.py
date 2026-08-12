from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram import Router

from mother.keyboards import verify_keyboard, verified_keyboard
from mother.services import get_one_user



router = Router()

@router.message(StateFilter(None),CommandStart())
async def handler_start(message: Message):
    user = await get_one_user(message.from_user)
    if user != "verified":
        await message.answer("🌚", reply_markup=verify_keyboard)
    else:
        await message.answer("🌚", reply_markup=verified_keyboard)