from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

from runtime.sync import sync_bots
from runtime.manager import shutdown_bots
from gateway.webhook import process_child_update

@asynccontextmanager
async def lifespan(app: FastAPI):
    await sync_bots()
    yield
    await shutdown_bots()

app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook/{bot_id}")
async def child_webhook(bot_id: int,request: Request):
    data = await request.json()
    await process_child_update(bot_id,data)
    return {"ok": True}