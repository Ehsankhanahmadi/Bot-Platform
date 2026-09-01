from contextlib import asynccontextmanager
from fastapi import FastAPI,Request

from webhook import process_update,set_webhook,shutdown
from assignments import assign_all_bots

from services.bot import database, runtimes

@asynccontextmanager
async def lifespan(app: FastAPI):
    await assign_all_bots(database, runtimes)
    await set_webhook()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook")
async def mother_webhook(request: Request):
    data = await request.json()
    await process_update(data)
    return {"ok": True}