from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram import F

from mother.services import get_all_bot, get_all_active_bot, get_all_inactive_bot, get_bot_by_id
from mother.keyboards import config_keyboard, create_bot_keyboard, create_detail_bot_keyboard

from . import router



@router.message(StateFilter(None),F.text == "⚙️ تنظیمات بات")
async def handler_config_bots(message:Message):
    all_bot = await get_all_bot(message.from_user.id)
    if all_bot:
        await message.answer("در این بخش میتوانید ربات های خود را مدیریت کنید", reply_markup=config_keyboard)
    else:
        await message.answer("شما در حال حاضر هیچ رباتی ندارید")

@router.callback_query(StateFilter(None),F.data == "active")
async def handler_active_bot(callback: CallbackQuery):
    all_active_bot = await get_all_active_bot(callback.from_user.id)
    new_keyboards = create_bot_keyboard(all_active_bot)
    if all_active_bot:
        await callback.message.edit_text("لیست ربات های فعال شما : ", reply_markup=new_keyboards)
    else:
        await callback.message.edit_text("شما در حال حاضر هیچ ربات فعالی ندارید", reply_markup=new_keyboards)

@router.callback_query(StateFilter(None),F.data == "inactive")
async def handler_inactive_bot(callback: CallbackQuery):
    all_inactive_bot = await get_all_inactive_bot(callback.from_user.id)
    new_keyboards = create_bot_keyboard(all_inactive_bot)
    if all_inactive_bot:
        await callback.message.edit_text("لیست ربات های غیر فعال شما : ", reply_markup=new_keyboards)
    else:
        await callback.message.edit_text("شما در حال حاضر هیچ ربات غیر فعالی ندارید", reply_markup=new_keyboards)

@router.callback_query(StateFilter(None),F.data.startswith("bot:"))
async def handler_detail_bot(callback: CallbackQuery):
    bot_id = int(callback.data.split(":")[1])
    bot = await get_bot_by_id(bot_id)
    new_keyboard = create_detail_bot_keyboard(bot)
    if bot:
        await callback.message.edit_text(f"مایل هستید چه تغییراتی را در این ربات انجام دهید ؟\n\n{bot["bot_username"]} : ", reply_markup=new_keyboard)
    else:
        await callback.message.edit_text("این ربات یافت نشد", reply_markup=new_keyboard)

@router.callback_query(StateFilter(None),F.data == "config_bot")
async def handler_callback_keyboard(callback:CallbackQuery):
    await callback.message.edit_text("در این بخش میتوانید ربات های خود را مدیریت کنید", reply_markup=config_keyboard)