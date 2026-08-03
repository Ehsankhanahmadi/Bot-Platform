from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from mother.button.start_button import keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("سلام 👋\nWebhook با موفقیت کار می‌کند.", reply_markup=keyboard)