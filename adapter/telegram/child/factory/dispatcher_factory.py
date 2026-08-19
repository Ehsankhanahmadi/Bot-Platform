from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from telegram.redis.redis import redis
from .handler_loader import load_handlers



def create_dispatcher(bot_id:int,config:dict):
    storage = RedisStorage(redis=redis,key_builder=DefaultKeyBuilder(with_bot_id=True))
    dp = Dispatcher(storage=storage)
    #
    # اینجا Context اضافه می کنیم
    #
    dp.workflow_data.update({"bot_id":bot_id,"config":config})
    dp = load_handlers(dp,config)
    return dp