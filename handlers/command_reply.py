from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

builder = ReplyKeyboardBuilder()

builder.add(
    KeyboardButton(text="📚 Курсы"),
    KeyboardButton(text="📝 Моя регистрация"),
    KeyboardButton(text="⚙ Админ"),
)

builder.adjust(2,1)

keyboard = builder.as_markup(resize_keyboard=True)