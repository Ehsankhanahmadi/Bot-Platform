from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder



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

config_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ ربات های فعال", callback_data="active")],
        [InlineKeyboardButton(text="❌ ربات های غیر فعال", callback_data="inactive")]
    ]
)

def create_bot_keyboard(bots:None):
    builder = InlineKeyboardBuilder()
    if bots:
        for bot in bots:
            builder.button(text=f"{bot["bot_username"]}",callback_data=f"{bot["bot_username"]}")
        builder.button(text="🔙 بازگشت به منو قبل", callback_data="config_bot")
    else:
        builder.button(text="🔙 بازگشت به منو قبل", callback_data="config_bot")
    builder.adjust(1)
    return builder.as_markup()