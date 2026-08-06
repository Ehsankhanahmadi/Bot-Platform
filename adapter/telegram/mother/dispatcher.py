from aiogram import Dispatcher
from mother.handlers.start import router as start_router
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

dp.include_router(start_router)