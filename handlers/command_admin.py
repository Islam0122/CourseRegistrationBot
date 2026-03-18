from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from filter.filters import IsAdmin, ChatTypeFilter
from texts.text import ADMINS
from db.orm_get_students import orm_get_students_all
from db.orm_add_new_course import orm_add_course, orm_delete_course, get_all_course, orm_edit_course
from keyboards.command_inline import keyboard_back

router_admin = Router()
router_admin.message.filter(IsAdmin())

@router_admin.message(Command("admin"))
async def admin(message: Message):
    await message.answer(
        text=ADMINS
    )

@router_admin.message(Command("view_students"))
async def admin(message: Message, session: AsyncSession):
    students = await orm_get_students_all(session)
    if not students:
        await message.answer("Студентов нет❌")
        return
    text = "Список студентов\n\n"
    for student in students:
        text += (
            f"Студент номер: {student.course_id}\n"
            f"Имя: {student.name}\n"
            f"Возраст: {student.age}\n"
            f"Телефон: {student.phone}\n"
            f"Запись: {student.course_type}\n\n"
        )
    await message.answer(text)

class AddCourse(StatesGroup):
    new_course = State()
    choose_course = State()
    for_update_course = State()
    new_course_name = State()

@router_admin.message(Command("create_new_course"))
async def create_new_course(message: Message, state: FSMContext):
    await state.set_state(AddCourse.new_course)
    await message.answer("Введите название нового курса")

@router_admin.message(AddCourse.new_course)
async def add_course(message: Message, state: FSMContext, session: AsyncSession):
    await orm_add_course(session, name=message.text)
    await state.clear()
    await message.answer("Курс добавлен ✅")

@router_admin.message(Command("delete_course"))
async def delete_course(message: Message, state: FSMContext, session: AsyncSession):
    courses = await get_all_course(session)
    if not courses:
        await message.answer("Курсов нет❌")
        return

    text = "Выберите курс для удаления\n\n"
    for course in courses:
        text += f"{course.course_id}: {course.course_name}\n"
    await state.set_state(AddCourse.choose_course)
    await message.answer(text)

@router_admin.message(AddCourse.choose_course)
async def choose_course(message: Message, state: FSMContext, session: AsyncSession):
    try:
        course_id = int(message.text)
    except:
        await message.answer("Введите ID числом ❌")
        return

    await orm_delete_course(session, course_id=course_id)
    await state.clear()
    await message.answer("Курс удалён ✅")

@router_admin.message(Command("update_course"))
async def update_course(message: Message, state: FSMContext, session: AsyncSession):
    courses = await get_all_course(session)
    if not courses:
        await message.answer("Курсов нет❌")
        return
    text = "Список актуальных курсов:\n\n"
    for course in courses:
        text += f"{course.course_id}: {course.course_name}\n\n"
    await state.update_data(course=courses)
    await state.set_state(AddCourse.for_update_course)
    await message.answer(text)

@router_admin.message(AddCourse.for_update_course)
async def update_course_handlers(message: Message, state: FSMContext, session: AsyncSession):
    await state.update_data(course_id=str(message.text))
    await state.set_state(AddCourse.new_course_name)
    await message.answer("Введите новое название курса:")

@router_admin.message(AddCourse.new_course_name)
async def new_course_handler(message: Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    course_id = data.get("course_id")
    new_name = message.text

    await orm_edit_course(session, course_id=course_id, course_name=new_name)
    await state.clear()
    await message.answer(text="Курс обнавлен✅", reply_markup=keyboard_back)





