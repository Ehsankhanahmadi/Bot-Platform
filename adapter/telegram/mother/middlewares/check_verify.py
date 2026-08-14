from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery

from ..services.user import get_one_user
from ..keyboards import verify_keyboard

from redis.asyncio import Redis



class CheckVerifyUserMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis):
            self.redis = redis

    async def __call__(self,handler,event: TelegramObject,data: dict):
        user = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        ban_key = f"ban:telegram:{user.id}"
        if await self.redis.get(ban_key) == "1":
            if isinstance(event, Message):
                await event.answer("🚫 شما به دلیل رعایت نکردن قوانین تا 24 ساعت آینده بن شدید.")
            elif isinstance(event, CallbackQuery):
                await event.answer("🚫 شما به دلیل رعایت نکردن قوانین تا 24 ساعت آینده بن شدید.",show_alert=True)
            return

        verify_key = f"verify:telegram:{user.id}"
        if await self.redis.get(verify_key) == "1":
            return await handler(event, data)

        user_main = await get_one_user(user)
        if user_main != "verified":
            spam_key = f"spam:telegram:{user.id}"
            count = await self.redis.incr(spam_key)
            if count == 1:
                await self.redis.expire(spam_key, 86400)
            if count > 15:
                await self.redis.set(ban_key,"1",ex=86400)
                if isinstance(event, Message):
                    await event.answer("🚫 شما به دلیل رعایت نکردن قوانین تا 24 ساعت آینده بن شدید.")
                elif isinstance(event, CallbackQuery):
                    await event.answer("🚫 شما به دلیل رعایت نکردن قوانین تا 24 ساعت آینده بن شدید.",show_alert=True)
                return
            if isinstance(event, Message):
                await event.answer("🌚", reply_markup=verify_keyboard)
            elif isinstance(event, CallbackQuery):
                await event.answer("🌚")
            return

        await self.redis.set(verify_key,"1",ex=86400)
        return await handler(event, data)