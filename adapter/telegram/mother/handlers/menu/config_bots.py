from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram import F, Bot
from aiogram.fsm.context import FSMContext

from mother.services import get_all_bot, get_all_active_bot, get_all_inactive_bot, get_bot_by_id, delete_bot_by_id, update_bot, status_change
from mother.keyboards import config_keyboard, create_bot_keyboard, create_detail_bot_keyboard, create_delete_bot_keyboard, create_custom_back
from mother.states import UserState

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

@router.callback_query(StateFilter(None),F.data.startswith("delete_bot"))
async def handler_delete_bot(callback: CallbackQuery):
    bot_id = int(callback.data.split(":")[1])
    bot = await get_bot_by_id(bot_id)
    new_keyboard = create_delete_bot_keyboard(bot)
    if bot:
        await callback.message.edit_text("اگر از حذف این ربات اطمینان دارید روی دکمه زیر کلیک کنید", reply_markup=new_keyboard)
    else:
        await callback.message.edit_text("این ربات یافت نشد", reply_markup=new_keyboard)

@router.callback_query(StateFilter(None),F.data.startswith("main_delete_bot"))
async def handler_main_delete_bot(callback: CallbackQuery):
    bot_id = int(callback.data.split(":")[1])
    bot_status = await delete_bot_by_id(bot_id)
    new_keyboard = create_custom_back(None)
    if bot_status:
        await callback.message.edit_text("ربات با موفقیت حذف شد", reply_markup=new_keyboard)
    else:
        await callback.message.edit_text("ربات مورد نظر یافت نشد", reply_markup=new_keyboard)

@router.callback_query(StateFilter(None),F.data.startswith("change_token"))
async def handler_change_token_bot(callback: CallbackQuery, state: FSMContext):
    bot_id = int(callback.data.split(":")[1])
    await callback.message.edit_text("لطفا توکن جدید خود را ارسال نمایید")
    await state.set_state(UserState.waiting_for_change_token)
    await state.update_data(bot_change=bot_id)

@router.message(UserState.waiting_for_change_token)
async def handler_main_change_token_bot(message:Message, state:FSMContext):
    checking_message = await message.answer("در حال بررسی توکن ...")
    token = message.text.strip()
    botid = await state.get_data()
    new_keyboard = create_custom_back(f"bot:{botid["bot_change"]}")
    try:
        bot = Bot(token=token)
        bot_info = await bot.get_me()
        bot_status = await update_bot(bot_info,token,message.from_user.id)
        if botid["bot_change"] == bot_info.id:
            if bot_status:
                await checking_message.edit_text(f"ربات شما با موفقیت اپدیت شد\n\ntoken : \n{token}\n\nusername : \n@{bot_info.username}")
            else:
                await checking_message.edit_text("ربات مورد نظر جهت اپدیت یافت نشد")
        await checking_message.edit_text("لطفا توکن مربوط به ربات مورد نظر را ارسال کنید توکن ارسال شده برای ربات مورد نظر نمی باشد",reply_markup=new_keyboard)
    except:
        await checking_message.edit_text("لطفا مجدد تلاش کنید توکن شما معتبر نمی باشد", reply_markup=new_keyboard)
    finally:
        if "bot" in locals():
            await bot.session.close()
    await state.clear()

@router.callback_query(StateFilter(None),F.data.startswith("deactivate_bot"))
async def handler_deactivate_bot(callback: CallbackQuery):
    bot_id = int(callback.data.split(":")[1])
    status = await status_change(bot_id, False)
    new_keyboard = create_custom_back(f"bot:{bot_id}")
    if status:
        await callback.message.edit_text("ربات مورد نظر غیر فعال شد", reply_markup=new_keyboard)
    else:
        await callback.message.edit_text("مشکلی در فرایند تغییر وضعیت به وجود امده است", reply_markup=new_keyboard)

@router.callback_query(StateFilter(None),F.data == "development_bot")
async def handler_delete_bot(callback: CallbackQuery):
    pass

@router.callback_query(StateFilter(None),F.data == "renew_bot")
async def handler_delete_bot(callback: CallbackQuery):
    pass

@router.callback_query(StateFilter(None),F.data.startswith("activate_bot"))
async def handler_activate_bot(callback: CallbackQuery):
    bot_id = int(callback.data.split(":")[1])
    status = await status_change(bot_id, True)
    new_keyboard = create_custom_back(f"bot:{bot_id}")
    if status:
        await callback.message.edit_text("ربات مورد نظر فعال شد", reply_markup=new_keyboard)
    else:
        await callback.message.edit_text("مشکلی در فرایند تغییر وضعیت به وجود امده است", reply_markup=new_keyboard)

@router.callback_query(StateFilter(None),F.data == "config_bot")
async def handler_callback_keyboard(callback:CallbackQuery):
    await callback.message.edit_text("در این بخش میتوانید ربات های خود را مدیریت کنید", reply_markup=config_keyboard)