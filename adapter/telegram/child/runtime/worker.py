from .registry import register_bot
from ..bot import create_bot
from ..dispatcher import get_dispatcher



async def create_bot_worker(token:str,bot_id:int,config:dict):
    bot = create_bot(token=token)
    dp = get_dispatcher(bot_id,config)
    webhook = (f"/telegram/webhook/{bot_id}")
    register_bot(bot_id=bot_id,bot=bot,dispatcher=dp,webhook=webhook)
    return {"bot":bot,"dispatcher":dp}