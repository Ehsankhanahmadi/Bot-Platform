from aiogram.types import Message, CallbackQuery
from aiogram import F

from mother.keyboards import read_help_keyboard

from . import router



@router.message(F.text == "🤖 ساخت بات")
async def handler_create_bots(message:Message):
    await message.answer("لطفا قبل از ساخت ربات خود بخش راهنما را مطالعه کنید تا با روند صحیح ساخت بات اشنا شوید در نهایت روی دکمه زیر کلیک کنید", reply_markup=read_help_keyboard)

@router.callback_query(F.data == "read_help")
async def handler_read_help(callback:CallbackQuery):
    await callback.message.answer("شما روی دکمه مطالعه کردم کلیک کردید")