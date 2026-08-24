from .registry import register_bot
from .ownership import claim_bot
from bot import create_bot
from dispatcher import get_dispatcher



async def create_bot_worker(token:str,bot_id:int,config:dict):
    owned = await claim_bot(bot_id)
    if not owned:
        return None
    bot = create_bot(token=token)
    dp = get_dispatcher(bot_id,config)
    webhook = (f"/telegram/webhook/{bot_id}")
    await register_bot(bot_id=bot_id,bot=bot,dispatcher=dp,webhook=webhook,config=config)
    return {"bot":bot,"dispatcher":dp}