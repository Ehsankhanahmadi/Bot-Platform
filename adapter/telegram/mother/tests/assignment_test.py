import asyncio

from assignments import assign_bot, get_assignment, remove_assignment

# runtimes = [
#     {
#         "runtime_id": "runtime-01",
#         "active": True,
#         "bot_count": 5000,
#     },
#     {
#         "runtime_id": "runtime-02",
#         "active": True,
#         "bot_count": 3000,
#     },
#     {
#         "runtime_id": "runtime-03",
#         "active": True,
#         "bot_count": 7000,
#     },
# ]

runtimes = [
    {
        "runtime_id": "runtime-01",
        "active": True,
        "bot_count": 5,
    },
    {
        "runtime_id": "runtime-02",
        "active": True,
        "bot_count": 2,
    },
]



async def main():
    # bot_id = 8718447220
    bot_1 = 8718447220
    bot_2 = 8620932466
    # runtime = await assign_bot(bot_id,runtimes)
    # print("Assigned Runtime:", runtime)

    # assignment = await get_assignment(bot_id)
    # print("Stored Assignment:", assignment)

    # removed = await remove_assignment(bot_id)
    # print("Removed:", removed)

    # assignment = await get_assignment(bot_id)
    # print("After Remove:", assignment)

    # Assign Bot 1
    runtime_1 = await assign_bot(bot_1, runtimes)
    print("Bot 1 Assigned Runtime:", runtime_1)

    assignment_1 = await get_assignment(bot_1)
    print("Bot 1 Stored Assignment:", assignment_1)

    # Assign Bot 2
    runtime_2 = await assign_bot(bot_2, runtimes)
    print("Bot 2 Assigned Runtime:", runtime_2)

    assignment_2 = await get_assignment(bot_2)
    print("Bot 2 Stored Assignment:", assignment_2)

    # Remove Bot 1
    removed_1 = await remove_assignment(bot_1)
    print("Bot 1 Removed:", removed_1)

    # Remove Bot 2
    removed_2 = await remove_assignment(bot_2)
    print("Bot 2 Removed:", removed_2)

    # Check after remove
    assignment_1 = await get_assignment(bot_1)
    assignment_2 = await get_assignment(bot_2)

    print("Bot 1 After Remove:", assignment_1)
    print("Bot 2 After Remove:", assignment_2)

asyncio.run(main())