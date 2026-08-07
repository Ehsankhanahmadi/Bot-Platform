from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from mother.keyboards.start import verify_keyboard



router = Router()

@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer("🌚", reply_markup=verify_keyboard)