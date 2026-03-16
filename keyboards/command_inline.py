from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

back = InlineKeyboardBuilder()
back.add(
    InlineKeyboardButton(text="⬅ Назад", callback_data="back"),
)
keyboard_back = back.as_markup()


further = InlineKeyboardBuilder()
further.add(
    InlineKeyboardButton(text="Далее", callback_data="further"),
)
further = further.as_markup()

registration_button = InlineKeyboardBuilder()
registration_button.add(
    InlineKeyboardButton(text="Подтвердить✅", callback_data="confirm"),
    InlineKeyboardButton(text="Отменить❌", callback_data="cancel"),
)
registration_button = registration_button.as_markup()

direction = InlineKeyboardBuilder()
direction.add(
    InlineKeyboardButton(text="Backend", callback_data="backend"),
    InlineKeyboardButton(text="Frontend", callback_data="frontend"),
)
directions = direction.as_markup()
