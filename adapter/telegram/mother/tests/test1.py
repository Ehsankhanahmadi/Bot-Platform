from assignments import select_runtime


runtimes = [
    {
        "runtime_id": "runtime-01",
        "active": False,
        "bot_count": 5000,
    },
    {
        "runtime_id": "runtime-02",
        "active": True,
        "bot_count": 3000,
    },
    {
        "runtime_id": "runtime-03",
        "active": True,
        "bot_count": 1000,
    },
]


runtime = select_runtime(runtimes)

print("Selected runtime:", runtime)