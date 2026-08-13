from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery

from ..services.user import get_one_user
from ..keyboards import verify_keyboard

from redis.asyncio import Redis
from mother.redis import redis



class CheckVerifyUserMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis):
            self.redis = redis

    async def __call__(self,handler,event: TelegramObject,data: dict):
        user = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        key = f"verify:telegram:{user.id}"
        cached = await self.redis.get(key)
        if cached == "1":
            return await handler(event, data)

        user_main = await get_one_user(user)
        if user_main != "verified":
            if isinstance(event, (Message, CallbackQuery)):
                await event.answer("🌚", reply_markup=verify_keyboard)
            return
        await self.redis.set(key,"1",ex=86400)
        return await handler(event, data)