from child.handlers import create_fallback_router



def load_handlers(dp,config):
    dp.include_router(create_fallback_router())

    return dp