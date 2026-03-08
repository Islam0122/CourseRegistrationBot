from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

back = InlineKeyboardBuilder()

back.add(
    InlineKeyboardButton(text="⬅ Назад", callback_data="back"),
)

keyboard_back = back.as_markup(resize_keyboard=True)