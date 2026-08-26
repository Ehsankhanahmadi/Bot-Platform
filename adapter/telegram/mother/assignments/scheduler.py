from typing import List, Dict, Optional


def select_runtime(runtimes: List[Dict]) -> Optional[str]:
    """
    Select the best available runtime.

    Strategy:
    - Ignore inactive runtimes.
    - Select the runtime with the lowest bot count.
    - Return None if no active runtime is available.
    """

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