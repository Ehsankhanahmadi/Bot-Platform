import httpx


class BackendClient:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
        )

    async def close(self):
        await self.client.aclose()