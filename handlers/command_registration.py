from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.command_inline import registration_button, keyboard_back
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_add_courses, check_registration

router_registration = Router()

class CommandRegistration(StatesGroup):
    name = State()
    age = State()
    phone = State()
    course = State()

@router_registration.callback_query(F.data == "further")
async def registration(query: CallbackQuery, state: FSMContext, session: AsyncSession):
    await query.message.answer(
        text="1️⃣ Как вас зовут?"
    )
    await state.set_state(CommandRegistration.name)

@router_registration.message(CommandRegistration.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("2️⃣ Сколько вам лет?")
    await state.set_state(CommandRegistration.age)

@router_registration.message(CommandRegistration.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("3️⃣ Ваш номер телефона?")
    await state.set_state(CommandRegistration.phone)

@router_registration.message(CommandRegistration.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("4️⃣ Какой курс вас интересует?")
    await state.set_state(CommandRegistration.course)

@router_registration.message(CommandRegistration.course)
async def get_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)

    info = await state.get_data()

    await message.answer(
        text=(
            f"Завершение регистрации✅\n"
            f"Имя: {info['name']}\n"
            f"Возраст: {info['age']}\n"
            f"Телефон: {info['phone']}\n"
            f"Выбор курса: {info['course']}"
        ),
        reply_markup=registration_button
    )

@router_registration.callback_query(F.data == "confirm")
async def confirm(query: CallbackQuery, state: FSMContext,session: AsyncSession,):

    info = await state.get_data()

    check = await check_registration(
        session,
        name=info['name'],
        course_type=info["course"]
    )

    if check:
        await query.message.answer(
            text="Вы уже зарегистрированы",
            reply_markup=keyboard_back
        )
        return

    new_course = await orm_add_courses(
        session=session,
        telegram_id=query.from_user.id,
        name=info['name'],
        age=info['age'],
        phone=info['phone'],
        course_type=info['course']
    )
    await state.clear()

    await query.message.answer(
        text="Регистрация успешно завершена✅",
        reply_markup=keyboard_back
    )

@router_registration.callback_query(F.data == "cancel")
async def cancel(query: CallbackQuery, state: FSMContext):
    await query.message.answer(
        text="Регистрация отменена❌",
        reply_markup=keyboard_back
    )
    await state.clear()