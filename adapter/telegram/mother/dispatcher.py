from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from .redis import redis

from mother.handlers import protected_router, verify_router, fallback_router



storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)

dp.include_router(verify_router)
dp.include_router(protected_router)
dp.include_router(fallback_router)