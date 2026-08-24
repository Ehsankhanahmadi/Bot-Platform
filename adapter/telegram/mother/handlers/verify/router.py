from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram import Router, F

from cache.redis import redis
from keyboards.keyboard import verified_keyboard
from services import verify_user

router = Router()



@router.message(StateFilter(None),F.contact)
async def handler_verify_user(message: Message):
    if message.contact.user_id != message.from_user.id:
        await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل بررسی نمی باشد 🧐")
        return

    checking_message = await message.answer("در حال بررسی ...")
    user = await verify_user(message.from_user,message.contact.phone_number)
    
    if user == "user added":
        await redis.set(f"botplatform:telegram:mother:verify:{message.from_user.id}","1",ex=86400)
        await checking_message.delete()
        await message.answer("✅ احراز هویت شما با موفقیت انجام شد",reply_markup=verified_keyboard)
    elif user == "verified":
        await redis.set(f"botplatform:telegram:mother:verify:{message.from_user.id}","1",ex=86400)
        await checking_message.delete()
        await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل بررسی نمی باشد 🧐",reply_markup=verified_keyboard)
    else:
        await checking_message.delete()
        await message.answer("لطفا مجدد تلاش کنید.")