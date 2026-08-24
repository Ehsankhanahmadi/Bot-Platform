import time

from cache.redis import redis
from .lifecycle import RUNTIME_ID

LEASE_TTL = 30



def owner_key(bot_id: int) -> str:
    return f"botplatform:telegram:runtime:bot:{bot_id}:owner"


def lease_key(bot_id: int) -> str:
    return f"botplatform:telegram:runtime:bot:{bot_id}:lease"


async def claim_bot(bot_id: int) -> bool:
    key = owner_key(bot_id)
    claimed = await redis.set(key,RUNTIME_ID,nx=True,ex=LEASE_TTL,)
    if claimed:
        await redis.set(lease_key(bot_id),int(time.time()),ex=LEASE_TTL,)
        return True
    current_owner = await redis.get(key)
    return current_owner == RUNTIME_ID


async def renew_bot_lease(bot_id: int) -> bool:
    key = owner_key(bot_id)
    current_owner = await redis.get(key)
    if current_owner != RUNTIME_ID:
        return False
    await redis.expire(key, LEASE_TTL)
    await redis.set(lease_key(bot_id),int(time.time()),ex=LEASE_TTL,)
    return True


async def release_bot(bot_id: int) -> bool:
    key = owner_key(bot_id)
    current_owner = await redis.get(key)
    if current_owner != RUNTIME_ID:
        return False
    await redis.delete(owner_key(bot_id),lease_key(bot_id),)
    return True


async def get_bot_owner(bot_id: int):
    return await redis.get(owner_key(bot_id))


async def is_bot_owner(bot_id: int) -> bool:
    current_owner = await redis.get(owner_key(bot_id))
    return current_owner == RUNTIME_ID