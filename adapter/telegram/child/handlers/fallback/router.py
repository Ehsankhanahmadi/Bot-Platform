from aiogram import Router
from aiogram.types import Message



def create_fallback_router():

    router = Router()

    @router.message()
    async def handler_fallback(message: Message):
        await message.answer("لطفا از منو های ربات استفاده کنید این پیام قابل برسی نمی باشد 🧐")

    return router