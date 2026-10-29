import asyncio
from typing import Dict, Any



registry: Dict[int, Dict[str, Any]] = {}
registry_lock = asyncio.Lock()


async def register_bot(bot_id: int,bot,dispatcher,webhook: str,config: dict,):
    async with registry_lock:
        registry[bot_id] = {
            "bot": bot,
            "dispatcher": dispatcher,
            "webhook": webhook,
            "status": "running",
            "config": config,
        }


async def remove_bot(bot_id: int):
    async with registry_lock:
        registry.pop(bot_id, None)


async def get_bot(bot_id: int):
    async with registry_lock:
        return registry.get(bot_id)


async def get_all_bots():
    async with registry_lock:
        return dict(registry)


async def update_status(bot_id: int, status: str):
    async with registry_lock:
        if bot_id in registry:
            registry[bot_id]["status"] = status