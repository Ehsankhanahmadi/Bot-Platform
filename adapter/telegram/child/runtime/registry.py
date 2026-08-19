from typing import Dict, Any
import asyncio



registry: Dict[int, Dict[str, Any]] = {}
registry_lock = asyncio.Lock()


async def register_bot(bot_id:int,bot,dispatcher,webhook:str,config:dict):
    async with registry_lock:
        registry[bot_id] = {
            "bot": bot,
            "dispatcher": dispatcher,
            "webhook": webhook,
            "status": "running",
            "config": config
        }


def remove_bot(bot_id:int):
    if bot_id in registry:
        del registry[bot_id]


def get_bot(bot_id:int):
    return registry.get(bot_id)


def get_all_bots():
    return registry


def update_status(bot_id:int,status:str):
    if bot_id in registry:
        registry[bot_id]["status"] = status