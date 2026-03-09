from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.types import CallbackQuery

back = InlineKeyboardBuilder()

back.add(
    InlineKeyboardButton(text="⬅ Назад", callback_data="back"),
)

keyboard_back = back.as_markup(resize_keyboard=True)



@router.callback_query()
async def callbacks(callback: CallbackQuery):

    if callback.data == "confirm":
        await callback.message.answer("✅ Вы зарегистрированы!")

    elif callback.data == "cancel":
        await callback.message.answer("❌ Регистрация отменена")

    elif callback.data == "back":
        await callback.message.answer(
            "Главное меню",
            reply_markup=main_menu
        )