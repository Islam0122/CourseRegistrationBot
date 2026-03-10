from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back = InlineKeyboardBuilder()
back.add(
    InlineKeyboardButton(text="⬅ Назад", callback_data="back"),
)
keyboard_back = back.as_markup()


direction = InlineKeyboardBuilder()
direction.add(
    InlineKeyboardButton(text="Backend", callback_data="backend"),
    InlineKeyboardButton(text="Frontend", callback_data="frontend"),
)
directions = direction.as_markup()
