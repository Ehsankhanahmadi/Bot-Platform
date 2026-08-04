from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()

builder.button(text="ثبت نام")
builder.button(text="ربات‌ها")
builder.button(text="ساخت ربات")
builder.button(text="تنظیمات")

builder.adjust(2, 2)

keyboard = builder.as_markup(
    resize_keyboard=True
)