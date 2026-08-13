from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram import Router

from mother.keyboards import verified_keyboard

router = Router()



@router.message(StateFilter(None),CommandStart())
async def handler_start(message: Message):
        await message.answer("🌚", reply_markup=verified_keyboard)