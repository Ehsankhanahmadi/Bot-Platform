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


def create_custom_back_keyboard(callback:str|None):
    builder = InlineKeyboardBuilder()
    if callback:
        builder.button(text="🔙 بازگشت به منو قبل", callback_data=f"{callback}")
    else:
        builder.button(text="🔙 بازگشت به منو قبل", callback_data="config_bot")
    builder.adjust(1)
    return builder.as_markup()


def create_bot_keyboard(bots:None):
    builder = InlineKeyboardBuilder()
    if bots:
        for bot in bots:
            builder.button(text=f"{bot["bot_username"]}",callback_data=f"bot:{bot["bot_id"]}")
        builder.button(text="🔙 بازگشت به منو قبل", callback_data="config_bot")
    else:
        builder.button(text="🔙 بازگشت به منو قبل", callback_data="config_bot")
    builder.adjust(1)
    return builder.as_markup()


def create_detail_bot_keyboard(bot:None):
    builder = InlineKeyboardBuilder()
    if not bot:
        return builder.as_markup()
    if bot["active"]:
        builder.button(text="💀 حذف بات",callback_data=f"delete_bot:{bot['bot_id']}")
        builder.button(text="🔑 تغییر توکن بات",callback_data=f"change_token:{bot['bot_id']}")
        builder.button(text="🔴 غیرفعال کردن بات",callback_data=f"deactivate_bot:{bot['bot_id']}")
        builder.button(text="🔵 حالت توسعه بات",callback_data=f"development_bot:{bot['bot_id']}")
        builder.button(text="💳 تمدید بات",callback_data=f"renew_bot:{bot['bot_id']}")
        builder.button(text="🔙 بازگشت به منو قبل",callback_data="active")
    else:
        builder.button(text="💀 حذف بات",callback_data=f"delete_bot:{bot['bot_id']}")
        builder.button(text="🟢 فعال کردن بات",callback_data=f"activate_bot:{bot['bot_id']}")
        builder.button(text="💳 تمدید بات",callback_data=f"renew_bot:{bot['bot_id']}")
        builder.button(text="🔙 بازگشت به منو قبل",callback_data="inactive")
    builder.adjust(1)
    return builder.as_markup()


def create_delete_bot_keyboard(bot:None):
    builder = InlineKeyboardBuilder()
    if bot:
        builder.button(text="💀 حذف ربات",callback_data=f"main_delete_bot:{bot["bot_id"]}")
        builder.button(text="🔙 بازگشت به منو قبل",callback_data=f"bot:{bot["bot_id"]}")
    else:
        builder.button(text="🔙 بازگشت به منو قبل",callback_data=f"bot:{bot["bot_id"]}")
    builder.adjust(1)
    return builder.as_markup()