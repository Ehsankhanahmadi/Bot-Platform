from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from mother.handlers import protected_router, start_router, verify_router, fallback_router



storage = MemoryStorage()

dp = Dispatcher(storage=storage)

dp.include_router(start_router)
dp.include_router(verify_router)
dp.include_router(protected_router)
dp.include_router(fallback_router)