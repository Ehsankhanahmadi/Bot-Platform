from typing import List, Dict, Optional



def select_runtime(runtimes: List[Dict]) -> Optional[str]:
    available_runtimes = [
        runtime
        for runtime in runtimes
        if runtime.get("active", False)
    ]

    if not available_runtimes:
        return None

    selected_runtime = min(
        available_runtimes,
        key=lambda runtime: runtime.get("bot_count", 0),
    )

    return selected_runtime["runtime_id"]