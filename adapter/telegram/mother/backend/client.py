import httpx

from config.settings import settings



class BackendClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=settings.backend_base_url,
            timeout=settings.backend_timeout,
            headers={
                "Runtime": (
                    f"{settings.runtime}"
                ),
                "Password": (
                    f"{settings.backend_password}"
                ),
                "Authorization": (
                    f"Bearer {settings.backend_token.get_secret_value()}"
                ),
                "Accept": "application/json",
            },
        )

    async def close(self):
        await self.client.aclose()


backend_client = BackendClient()