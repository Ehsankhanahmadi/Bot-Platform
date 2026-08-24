import asyncio

from .ownership import renew_bot_lease

RENEW_INTERVAL = 10



class LeaseManager:
    def __init__(self):
        self.bot_ids: set[int] = set()
        self._task: asyncio.Task | None = None

    def add_bot(self, bot_id: int):
        self.bot_ids.add(bot_id)

    def remove_bot(self, bot_id: int):
        self.bot_ids.discard(bot_id)

    async def renew_all(self):
        for bot_id in list(self.bot_ids):
            try:
                renewed = await renew_bot_lease(bot_id)
                if renewed:
                    print(f"[LEASE] Bot {bot_id} lease renewed ✅")
                else:
                    print(f"[LEASE] Bot {bot_id} lease lost ❌")
                    self.remove_bot(bot_id)
                    from .manager import stop_bot
                    await stop_bot(bot_id)
            except Exception as e:
                print(f"[LEASE] Bot {bot_id} renewal error: {e}")

    async def run(self):
        while True:
            await self.renew_all()
            await asyncio.sleep(RENEW_INTERVAL)

    def start(self):
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self.run())

    async def stop(self):
        if self._task is not None:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None