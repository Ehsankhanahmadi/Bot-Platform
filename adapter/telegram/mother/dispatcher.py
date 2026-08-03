from aiogram import Dispatcher
from mother.handlers.start import router as start_router

dp = Dispatcher()

dp.include_router(start_router)