from .scheduler import select_runtime
# from .repository import save_assignment, get_assignment_runtime, delete_assignment



async def assign_bot(bot_id: int, runtimes: list[dict]):
    runtime_id = select_runtime(runtimes)
    if runtime_id is None:
        return None
    # saved = await save_assignment(bot_id=bot_id,runtime_id=runtime_id,)
    # if not saved:
    #     return None
    # print(f"[ASSIGNMENT] Bot {bot_id} assigned to {runtime_id} ✅")
    # for i in runtimes:
    #     if i["runtime_id"] == runtime_id:
    #         i["bot_count"] += 1
    # return runtime_id


async def assign_all_bots(bots: list[dict],runtimes: list[dict]):
    for bot in bots:
        if not bot.get("active", False):
            continue
        if bot.get("assignment") is not None:
            print(f"[ASSIGNMENT] Bot {bot['bot_id']} already assigned to {bot['assignment']} → skipping...")
            continue
        runtime_id = await assign_bot(bot["bot_id"],runtimes)
        if runtime_id is None:
            print(f"[ASSIGNMENT] Bot {bot['bot_id']} could not be assigned ❌")
            continue


# async def get_assignment(bot_id: int):
#     return await get_assignment_runtime(bot_id)


# async def remove_assignment(bot_id: int):
#     return await delete_assignment(bot_id)