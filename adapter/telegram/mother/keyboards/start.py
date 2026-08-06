from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()

builder.button(text="ساخت بات")
builder.button(text="تنظیمات بات")
builder.button(text="راهنما")

builder.adjust(2, 1)

keyboardstart = builder.as_markup(
    resize_keyboard=True
)