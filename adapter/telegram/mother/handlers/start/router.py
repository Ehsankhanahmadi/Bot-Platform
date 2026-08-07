from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from mother.keyboards.start import keyboardstart



router = Router()

@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer("🌚", reply_markup=keyboardstart)