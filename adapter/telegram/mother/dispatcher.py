from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from mother.handlers.start import router as start_router
from mother.handlers.verify import router as verify_router
from mother.handlers.protected import router as protected_router
from mother.handlers.fallback import router as fallback_router



storage = MemoryStorage()

dp = Dispatcher(storage=storage)

dp.include_router(start_router)
dp.include_router(verify_router)
dp.include_router(protected_router)
dp.include_router(fallback_router)