from aiogram.types import Message
from aiogram import F

from mother.keyboards.start import verified_keyboard
from mother.services import register_user

from . import router

@router.message(F.contact)
async def handler_verify_user(message: Message):
    user = await register_user(message.from_user)
    await message.answer("✅ شما با موفقیت تایید شدید", reply_markup=verified_keyboard)