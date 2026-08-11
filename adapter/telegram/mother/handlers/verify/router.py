from aiogram.types import Message
from aiogram import Router, F

from mother.keyboards import verified_keyboard
from mother.services import verify_user

router = Router()



@router.message(F.contact)
async def handler_verify_user(message: Message):
    if message.contact.user_id == message.from_user.id:
        checking_message = await message.answer("در حال بررسی ...")
        user = await verify_user(message.from_user, message.contact.phone_number)
        if user != "verified":
            await checking_message.edit_text("✅ احراز هویت شما با موفقیت انجام شد", reply_markup=verified_keyboard)
        else:
            await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل برسی نمی باشد 🧐", reply_markup=verified_keyboard)
    else:
        await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل برسی نمی باشد 🧐")