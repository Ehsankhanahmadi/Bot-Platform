from contextlib import asynccontextmanager
from fastapi import FastAPI,Request

from .webhook import process_update,set_webhook,shutdown

from child.runtime.sync import sync_bots
from child.runtime.webhook import process_child_update


@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_webhook()
    await sync_bots()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook")
async def mother_webhook(request: Request):
    data = await request.json()
    await process_update(data)
    return {"ok": True}


@app.post("/telegram/webhook/{bot_id}")
async def child_webhook(bot_id: int,request: Request):
    data = await request.json()
    await process_child_update(bot_id,data)
    return {"ok": True}