import asyncio

from .assignment import get_bot_assignment
from .lifecycle import RUNTIME_ID
from .ownership import claim_bot
from .manager import start_bot
from .lease import LeaseManager

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



lease_manager = LeaseManager()


async def sync_bots():
    tasks = []
    for bot_config in database:
        if not bot_config["active"]:
            continue
        bot_id = bot_config["bot_id"]
        assigned_runtime = await get_bot_assignment(bot_id)
        if assigned_runtime != RUNTIME_ID:
            print(f"[SYNC] Bot {bot_id} assigned to {assigned_runtime} skipping...")
            continue
        claimed = await claim_bot(bot_id)
        if not claimed:
            print(f"[SYNC] Bot {bot_id} "f"is owned by another runtime ❌")
            continue
        print(f"[SYNC] Bot {bot_id} "f"claimed by current runtime ✅")
        lease_manager.add_bot(bot_id)
        tasks.append(asyncio.create_task(start_bot(bot_config)))
    lease_manager.start()
    if tasks:
        await asyncio.gather(*tasks)