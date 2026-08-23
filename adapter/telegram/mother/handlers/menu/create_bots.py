from aiogram.types import Message, CallbackQuery
from aiogram import F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.keyboard import read_help_keyboard
from states.state import UserState
from services import create_bot

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
        bot = Bot(token=token)
        bot_info = await bot.get_me()
        bot_status = await create_bot(bot_info,token,message.from_user.id)
        if bot_status:
            await checking_message.edit_text(f"اطلاعات ربات شما ثبت شد :\n\ntoken : \n{token}\n\nusername : \n@{bot_info.username}")
        else:
            await checking_message.edit_text("این ربات قبلا ساخته شده است لطفا توکن جدیدی را وارد نمایید")
    except Exception as e:
        await checking_message.edit_text("لطفا مجدد تلاش کنید توکن شما معتبر نمی باشد")
    finally:
        if "bot" in locals():
            await bot.session.close()
    await state.clear()