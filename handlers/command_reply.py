from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

builder = ReplyKeyboardBuilder()

builder.add(
    KeyboardButton(text="📚 Курсы"),
    KeyboardButton(text="📝 Моя регистрация"),
    KeyboardButton(text="⚙ Админ"),
)

builder.adjust(2,1)

keyboard = builder.as_markup(resize_keyboard=True)
course_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подтвердить регистрацию", callback_data="confirm")],
        [InlineKeyboardButton(text="❌ Отменить регистрацию", callback_data="cancel")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]
)