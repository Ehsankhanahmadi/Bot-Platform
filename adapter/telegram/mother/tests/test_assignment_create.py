import asyncio

from assignments import assign_bot


runtimes = [
    {
        "runtime_id": "runtime-01",
        "active": True,
        "bot_count": 0,
    },
    {
        "runtime_id": "runtime-02",
        "active": True,
        "bot_count": 0,
    },
]


async def main():

    result_1 = await assign_bot(8718447220,runtimes)
    for i in runtimes:
        if i['runtime_id'] == result_1:
            i["bot_count"] += 1
    print("Bot 1 Assigned Runtime:",result_1)

    result_2 = await assign_bot(8620932466,runtimes)
    for i in runtimes:
        if i['runtime_id'] == result_2:
            i["bot_count"] += 1
    print("Bot 2 Assigned Runtime:",result_2)


asyncio.run(main())