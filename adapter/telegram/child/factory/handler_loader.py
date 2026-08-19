from child.handlers import fallback_router



def load_handlers(dp):
    dp.include_router(fallback_router)

    return dp