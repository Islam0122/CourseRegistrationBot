from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from keyboards.command_inline import keyboard_back
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_edit_course, get_user_courses

router_edit = Router()

class EditCourse(StatesGroup):
    new_course_name = State()
    choose_courses = State()

@router_edit.message(Command('edit_course'))
async def start_edit(message: Message, state: FSMContext, session: AsyncSession):

    courses = await get_user_courses(session, message.from_user.id)

    if not courses:
        await message.answer("У вас нет курсов для редактирования.")
        return

    text="Вы записывались на эти курсы\nВыберите курс для редактирования\n"
    for c in courses:
        text += f"{c.course_id}: {c.course_type}\n"

    await state.update_data(courses=courses)
    await state.set_state(EditCourse.choose_courses)
    await message.answer(text)

@router_edit.message(EditCourse.choose_courses)
async def edit_course_handler(message: Message, state: FSMContext):
    await state.update_data(courses_id=str(message.text))
    await state.set_state(EditCourse.new_course_name)
    await message.answer("Введите новое название курса:")

@router_edit.message(EditCourse.new_course_name)
async def new_course_handler(message: Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    course_id = data["courses_id"]
    new_name = message.text

    await orm_edit_course(session, course_id=course_id, course_type=new_name)
    await state.clear()

    await message.answer(text="Курс обнавлен✅", reply_markup=keyboard_back)