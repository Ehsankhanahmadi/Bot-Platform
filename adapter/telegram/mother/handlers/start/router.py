from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from mother.states.user import UserState
from mother.keyboards.start import keyboardstart

router = Router()

@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer("سلام 👋\nWebhook با موفقیت کار می‌کند.", reply_markup=keyboardstart)

@router.message(F.text == "ساخت بات")
async def handler_create_bot_messages(message: Message, state: FSMContext):
    await state.set_state(UserState.waiting_for_token)
    await message.answer("لطفا توکن ربات خود را وارد کنید.")

@router.message(UserState.waiting_for_token)
async def handler_token_input(message: Message, state: FSMContext):
    token = message.text
    await state.update_data(token=token)
    await state.set_state(UserState.waiting_for_idbot)
    await message.answer(f"توکن شما دریافت شد: {token}\nلطفا آیدی بات خود را وارد کنید.")

@router.message(UserState.waiting_for_idbot)
async def handler_idbot_input(message: Message, state: FSMContext):
    idbot = message.text
    await state.update_data(idbot=idbot)
    data = await state.get_data()
    await message.answer(f"اطلاعات بات شما دریافت شد:\nتوکن: {data['token']}\nآیدی بات: {data['idbot']}")
    await state.clear() 