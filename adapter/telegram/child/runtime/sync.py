import asyncio
from .manager import start_bot
from mother.services.bot import database



async def sync_bots():
    tasks = []
    for bot_config in database:
        if bot_config["active"]:
            tasks.append(asyncio.create_task(start_bot(bot_config)))
    await asyncio.gather(*tasks)