from .scheduler import select_runtime
from .repository import save_assignment, get_assignment_runtime, delete_assignment



async def assign_bot(bot_id: int, runtimes: list[dict]):
    runtime_id = select_runtime(runtimes)
    if runtime_id is None:
        return None
    saved = await save_assignment(bot_id=bot_id,runtime_id=runtime_id,)
    if not saved:
        return None
    return runtime_id


async def get_assignment(bot_id: int):
    return await get_assignment_runtime(bot_id)


async def remove_assignment(bot_id: int):
    return await delete_assignment(bot_id)