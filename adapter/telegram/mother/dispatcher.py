from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from mother.handlers.start import router as start_router
from mother.handlers.menu import router as menu_router

from mother.middlewares.register_user import RegisterUserMiddleware



storage = MemoryStorage()

dp = Dispatcher(storage=storage)

dp.update.middleware(RegisterUserMiddleware())

dp.include_router(start_router)
dp.include_router(menu_router)