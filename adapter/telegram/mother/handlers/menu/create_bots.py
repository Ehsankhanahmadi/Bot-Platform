import os
import json
from aiogram.types import Message, CallbackQuery
from aiogram import F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.keyboard import read_help_keyboard
from states.state import UserState
from services import create_bot
from services.bot import runtimes
from assignments import assign_bot

import httpx

from . import router



@router.message(StateFilter(None),F.text == "🤖 ساخت بات")
async def handler_create_bots(message:Message):
    await message.answer("لطفا قبل از ساخت ربات خود بخش راهنما را مطالعه کنید تا با روند صحیح ساخت بات اشنا شوید در نهایت روی دکمه زیر کلیک کنید", reply_markup=read_help_keyboard)


@router.callback_query(StateFilter(None),F.data == "read_help")
async def handler_read_help(callback:CallbackQuery, state:FSMContext):
    await callback.message.edit_text("توکن را ارسال نمایید مثال : \n\n8165416477:AA4sd5f5dfs7ex0d9Me-44se7f8sdf6R8IKNDSYE")
    await state.set_state(UserState.waiting_for_token)


@router.message(UserState.waiting_for_token)
async def handler_give_token(message:Message, state:FSMContext):
    checking_message = await message.answer("در حال بررسی توکن ...")
    token = message.text.strip()
    try:
        bot = Bot(token)
        bot_info = await bot.get_me()
        bot_status = await create_bot(bot_info,token,message.from_user.id,True)
        if bot_status:
            runtime_id = await assign_bot(bot_info.id,runtimes)
            if runtime_id is None:
                print(f"[ASSIGNMENT] Bot {bot_info.id} could not be assigned ❌")
            data={
                "token": token,
                "bot_username": f"@{bot_info.username}",
                "bot_id": bot_info.id,
                "user_id": message.from_user.id,
                "active": True,
            }
            id = runtime_id.split("-")[1]
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{os.getenv(f"RUNTIME_URL_{id}")}/telegram/{runtime_id}", json=data)
                print(response,type(response))
            if response:
                print(f"[ASSIGNMENT] Bot {bot_info.id} started on {runtime_id} ✅")
                for runtime in runtimes:
                    if runtime["runtime_id"] == runtime_id:
                        runtime["bot_count"] += 1
                        break
                await checking_message.edit_text(f"اطلاعات ربات شما ثبت شد :\n\ntoken : \n{token}\n\nusername : \n@{bot_info.username}")
            else:
                print(f"[RUNTIME] Failed to start bot {bot_info.id} on {runtime_id} ❌")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.text}")
                await checking_message.edit_text("ربات هنگام اجرا دچار مشکل شده است")
        else:
            await checking_message.edit_text("این ربات قبلا ساخته شده است لطفا توکن جدیدی را وارد نمایید")
    except Exception as e:
        print(e)
        await checking_message.edit_text("لطفا مجدد تلاش کنید ارتباط با تلگرام با مشکل مواجه شد")
    finally:
        if "bot" in locals():
            await bot.session.close()
    await state.clear()