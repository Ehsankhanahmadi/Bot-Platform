import hashlib

from django.core.cache import cache

from core.models import RunTime

AUTH_CACHE_TIMEOUT = 120
CACHE_PREFIX = "runtime_auth"
VERSION_PREFIX = "runtime_auth_ver"



def _fingerprint(*parts: str) -> str:
    raw = ":".join(parts).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def get_runtime_version(runtime_id: str) -> int:
    return cache.get_or_set(f"{VERSION_PREFIX}:{runtime_id}", 1, timeout=None)


def bump_runtime_version(runtime_id: str) -> None:
    key = f"{VERSION_PREFIX}:{runtime_id}"
    try:
        cache.incr(key)
    except ValueError:
        cache.set(key, 1, timeout=None)


def get_runtime_cache_key(runtime_id: str, password: str, token: str) -> str:
    version = get_runtime_version(runtime_id)
    return f"{CACHE_PREFIX}:{version}:{runtime_id}:{_fingerprint(password, token)}"


def cache_runtime(runtime: RunTime, password: str, token: str) -> None:
    cache_key = get_runtime_cache_key(runtime.runtime_id, password, token)
    cache_data = {
        "pk": runtime.pk,
        "runtime_id": runtime.runtime_id,
        "status": runtime.status,
        "bot_count": runtime.bot_count,
    }
    cache.set(cache_key, cache_data, timeout=AUTH_CACHE_TIMEOUT)


def get_cached_runtime(runtime_id: str, password: str, token: str):
    cache_key = get_runtime_cache_key(runtime_id, password, token)
    cache_data = cache.get(cache_key)
    if not cache_data:
        return None
    runtime = RunTime(
        pk=cache_data["pk"],
        runtime_id=cache_data["runtime_id"],
        status=cache_data["status"],
        bot_count=cache_data["bot_count"],
    )
    runtime._state.adding = False
    runtime._state.db = "default"
    runtime.from_cache = True
    return runtime


def delete_runtime_cache(runtime_id: str) -> None:
    bump_runtime_version(runtime_id)