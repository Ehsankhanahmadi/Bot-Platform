from aiogram import Router
from aiogram.types import Message

router = Router()



@router.message()
async def handler_unknown_message(message: Message):
    await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل برسی نمی باشد 🧐")