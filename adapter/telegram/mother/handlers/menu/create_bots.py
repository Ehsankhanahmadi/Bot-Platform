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
    result = await create_bot(token=token, userid=message.from_user.id, status=True) 
    if not result["success"]: 
        reason = result["reason"] 
        if reason == "already_exists": 
            await checking_message.edit_text("این ربات قبلا ساخته شده است لطفا توکن جدیدی را وارد نمایید") 
        elif reason == "invalid_token": 
            await checking_message.edit_text( "توکن وارد شده معتبر نیست" ) 
        elif reason == "telegram_error": 
            await checking_message.edit_text("لطفا مجدد تلاش کنید سرور تلگرام در دسترس نمی باشد") 
        else: 
            await checking_message.edit_text("هنگام ساخت ربات مشکلی به وجود آمد") 
            return 
    bot_info = result["bot"] 
    print(f"[BOT] Bot {bot_info.id} created successfully ✅") 
    runtime_id = await assign_bot(bot_info.id, runtimes) 
    if runtime_id is None: 
        print(f"[ASSIGNMENT] Bot {bot_info.id} could not be assigned ❌") 
        await checking_message.edit_text("ربات با موفقیت ساخته شد ولی در اجرای ربات مشکلی پیش امده است با پشتیبانی تماس بگیرید") 
        return 
    print(f"[ASSIGNMENT] Bot {bot_info.id} assigned to {runtime_id} ✅") 
    data = { 
        "token": token, 
        "bot_username": f"@{bot_info.username}", 
        "bot_id": bot_info.id, 
        "user_id": message.from_user.id, 
        "active": True
    } 
    runtime_number = runtime_id.split("-")[-1] 
    runtime_url = os.getenv(f"RUNTIME_URL_{runtime_number}") 
    if not runtime_url: 
        print(f"[RUNTIME] URL not found for {runtime_id} ❌") 
        await checking_message.edit_text("آدرس سرور اجرای ربات پیدا نشد") 
        return 
    try: 
        async with httpx.AsyncClient() as client: 
            response = await client.post( f"{runtime_url}/telegram/{runtime_id}", json=data, timeout=10) 
            print(f"[RUNTIME] Response: {response.status_code} {response.text}") 
            if response.is_success: 
                print(f"[RUNTIME] Bot {bot_info.id} started on {runtime_id} ✅") 
                await checking_message.edit_text(f"اطلاعات ربات شما ثبت شد :\n\ntoken : \n{token}\n\nusername : \n@{bot_info.username}") 
            else: 
                print(f"[RUNTIME] Failed to start bot {bot_info.id} ❌") 
                await checking_message.edit_text("ربات با موفقیت ساخته شد ولی در هنگام اجرا در سرور مورد نظر با مشکل مواجه شد") 
    except httpx.RequestError as e: 
        print(f"[RUNTIME] Connection error: {e}") 
        await checking_message.edit_text("لطفا کمی بعد تلاش کنید سروری در دسترس نیست") 
    except httpx.HTTPError as e: 
        print(f"[RUNTIME] HTTP error: {e}") 
        await checking_message.edit_text("مشکلی در ارتباط به سرور به وجود امده است") 
    await state.clear()