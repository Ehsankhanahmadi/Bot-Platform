from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

from .webhook import process_update, shutdown
from .runtime.sync import sync_bots


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Runtime starting...")
    await sync_bots()
    print("Bots synced ✅")
    yield
    await shutdown()


app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook/{bot_id}")
async def telegram_webhook(bot_id:int,request:Request):
    data = await request.json()
    await process_update(bot_id,data)
    return {"ok":True}