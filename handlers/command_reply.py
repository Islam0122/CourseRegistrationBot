from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Курсы"),
        KeyboardButton(text="📝 Моя регистрация")],
        [KeyboardButton(text="⚙ Админ")]
    ],
    resize_keyboard=True
)
