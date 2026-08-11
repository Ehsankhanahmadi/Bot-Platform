from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



verify_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 احراز هویت",request_contact=True)],
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

read_help_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="راهنما را مطالعه کردم", callback_data="read_help", style="success")],
    ],
)