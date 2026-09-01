import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from runtime.manager import start_bot
from runtime.sync import sync_bots, lease_manager
from runtime.manager import shutdown_bots
from gateway.webhook import process_child_update
from runtime.ownership import claim_bot
from runtime.assignment import get_bot_assignment
from runtime.lifecycle import RUNTIME_ID

@asynccontextmanager
async def lifespan(app: FastAPI):
    await sync_bots()
    yield
    await shutdown_bots()

class BotModel(BaseModel):
    token: str
    bot_username: str
    bot_id: int
    user_id: int
    active: bool

app = FastAPI(lifespan=lifespan)



@app.post("/telegram/webhook/{bot_id}")
async def child_webhook(bot_id: int,request: Request):
    data = await request.json()
    await process_child_update(bot_id,data)
    return {"ok": True}


@app.post("/telegram/{runtime_id}")
async def run_new_bot(runtime_id: str, data: BotModel):
    print(data,type(data))
    main_runtime_id = os.getenv("RUNTIME_ID")
    if runtime_id != main_runtime_id:
        return JSONResponse(status_code=403,content={"error": "runtime mismatch",})
    bot_config = {
        "token": data.token,
        "bot_username": data.bot_username,
        "bot_id": data.bot_id,
        "user_id": data.user_id,
        "active": data.active,
    }
    try:
        bot_id = data.bot_id
        assigned_runtime = await get_bot_assignment(bot_id)
        if assigned_runtime != RUNTIME_ID:
            print(f"[SYNC] Bot {bot_id} assigned to {assigned_runtime} skipping...")
        claimed = await claim_bot(bot_id)
        if not claimed:
            print(f"[SYNC] Bot {bot_id} "f"is owned by another runtime ❌")
        print(f"[SYNC] Bot {bot_id} "f"claimed by current runtime ✅")
        lease_manager.add_bot(bot_id)
        result = await start_bot(bot_config)
        if result:
            return {"status": True,"bot_id": data.bot_id}
        return JSONResponse(status_code=500,content={"status": False,"error": "start_bot returned False",})
    except Exception as e:
        import traceback
        return JSONResponse(status_code=500,content={"status": False,"error": repr(e)})