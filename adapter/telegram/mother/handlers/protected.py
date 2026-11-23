from aiogram import Router

from middlewares.check_verify import CheckVerifyUserMiddleware
from cache.redis import redis

from .menu import router as menu_router
from .start import router as start_router

router = Router()



router.message.middleware(CheckVerifyUserMiddleware(redis))
router.callback_query.middleware(CheckVerifyUserMiddleware(redis))

router.include_router(menu_router)
router.include_router(start_router)