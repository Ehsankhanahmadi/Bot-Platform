from cache.redis import redis

ASSIGNMENT_PREFIX = "botplatform:telegram:assignment:bot"



def assignment_key(bot_id: int) -> str:
    return f"{ASSIGNMENT_PREFIX}:{bot_id}"


async def save_assignment(bot_id: int, runtime_id: str) -> bool:
    key = assignment_key(bot_id)
    result = await redis.set(key, runtime_id)
    return bool(result)


async def get_assignment_runtime(bot_id: int):
    key = assignment_key(bot_id)
    return await redis.get(key)


async def delete_assignment(bot_id: int) -> bool:
    key = assignment_key(bot_id)
    result = await redis.delete(key)
    return result > 0