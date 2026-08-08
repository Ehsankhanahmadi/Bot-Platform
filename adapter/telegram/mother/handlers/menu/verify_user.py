from aiogram.types import Message
from aiogram import F

from mother.keyboards import verified_keyboard
from mother.services import verify_user

from . import router



@router.message(F.contact)
async def handler_verify_user(message: Message):
    if message.contact.user_id == message.from_user.id:
        user = await verify_user(message.from_user)
        await message.answer("✅ احراز هویت شما با موفقیت انجام شد", reply_markup=verified_keyboard)
    else:
        await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل برسی نمی باشد 🧐")