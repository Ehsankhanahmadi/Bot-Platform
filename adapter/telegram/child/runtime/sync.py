import asyncio
from .manager import start_bot

database = [
    {
        "token":'8718447220:AAFUFTbQ_BZVhLsrcoXIwBx1ehcvHEfyWGI',
        "bot_username": "@sdcsdfswefwef_bot",
        "bot_id": 8718447220,
        "user_id": 6247073627,
        "active": True
    },
    {
        "token":'8620932466:AAHpUgtbBICRBsp_dYsRDWGMyBCHK8Fb_mE',
        "bot_username": "@sdgfsddgr_bot",
        "bot_id": 8620932466,
        "user_id": 6247073627,
        "active": True
    }
]


async def sync_bots():
    tasks = []
    for bot_config in database:
        if bot_config["active"]:
            tasks.append(asyncio.create_task(start_bot(bot_config)))
    if tasks:
        await asyncio.gather(*tasks)