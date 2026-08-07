from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from ..services import register_user


class RegisterUserMiddleware(BaseMiddleware):
    async def __call__(self,handler,event: TelegramObject,data: dict):
        user = data.get("event_from_user")
        if user:
            try:
                await register_user(user)
            except Exception as e:
                print(f"Error occurred while registering user: {e}")
        return await handler(event, data)