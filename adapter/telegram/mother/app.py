from contextlib import asynccontextmanager
from fastapi import FastAPI,Request

from webhook import process_update,set_webhook,shutdown

@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_webhook()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook")
async def mother_webhook(request: Request):
    data = await request.json()
    await process_update(data)
    return {"ok": True}