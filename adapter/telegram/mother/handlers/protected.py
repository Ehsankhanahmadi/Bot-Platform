from aiogram import Router

from mother.middlewares.check_verify import CheckVerifyUserMiddleware

from .menu import router as menu_reuter



router = Router()

router.message.middleware(CheckVerifyUserMiddleware())
router.callback_query.middleware(CheckVerifyUserMiddleware())

router.include_router(menu_reuter)