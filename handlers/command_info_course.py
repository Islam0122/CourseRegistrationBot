from aiogram import Router, F
from aiogram.types import Message,FSInputFile
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_add_new_course import get_all_course
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

router_info_course = Router()

@router_info_course.message(F.text == "📚 Курсы")
async def info_course(message: Message, session: AsyncSession):
    info = await get_all_course(session)
    if not info:
        await message.answer("Курсов нет❌")
        return
    number = 0
    direction = InlineKeyboardBuilder()
    for course in info:
        number += 1
        direction.add(
            InlineKeyboardButton(text=course.course_name, callback_data=course.course_name)
        )
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption="Список наших курсов:\n\n",
        reply_markup=direction.as_markup(),
    )