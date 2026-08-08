from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton



verify_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 ارسال شماره موبایل",request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

verified_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⚙️ تنظیمات بات"),KeyboardButton(text="🤖 ساخت بات")],
        [KeyboardButton(text="🆘 راهنما")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)