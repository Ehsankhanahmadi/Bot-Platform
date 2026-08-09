from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from ..services.user import get_one_user
from ..keyboards import verify_keyboard



class CheckVerifyUserMiddleware(BaseMiddleware):
    async def __call__(self,handler,event: TelegramObject,data: dict):
        user = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        user_main = await get_one_user(user)

        if user_main != "verified":
            if isinstance(event, Message):
                await event.answer("🌚", reply_markup=verify_keyboard)
            return

        return await handler(event, data)