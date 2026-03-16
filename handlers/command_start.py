from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_add_user
from texts.text import TEXT_START, TEXT_HELP, ABOUT_ACADEMY, ABOUT_BOT, ABOUT_COURSE, REGISTRATION, ADMINS
from keyboards.command_reply import keyboard
from keyboards.command_inline import keyboard_back, directions, further, registration_button

router_start = Router()

@router_start.message(Command('start'))
async def start(message: Message, session: AsyncSession):
    await orm_add_user(session, message.from_user.id, message.from_user.username)
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=TEXT_START,
        reply_markup=keyboard
    )

@router_start.callback_query(F.data == "back")
async def back(query: CallbackQuery):
    await query.message.answer(
        text=TEXT_START,
    )

@router_start.message(Command('help'))
async def helping(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=TEXT_HELP,
        reply_markup=keyboard_back
    )

@router_start.message(Command('about_academy'))
async def about(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ABOUT_ACADEMY,
        reply_markup=keyboard_back
    )

@router_start.message(Command('about_bot'))
async def about_bot(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ABOUT_BOT,
        reply_markup=keyboard_back
    )

@router_start.message(F.text == "📚 Курсы")
async def about_course(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ABOUT_COURSE,
        reply_markup=directions
    )

@router_start.message(F.text == "📝 Моя регистрация")
async def registration(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=REGISTRATION,
        reply_markup=further
    )

@router_start.message(F.text == "⚙ Админ")
async def admin(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ADMINS,
        reply_markup=keyboard_back
    )