from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from texts.text import TEXT_START, TEXT_HELP, ABOUT_ACADEMY, ABOUT_BOT

router_start = Router()

@router_start.message(Command('start'))
async def start(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=TEXT_START
    )

@router_start.message(Command('help'))
async def helping(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=TEXT_HELP
    )

@router_start.message(Command('about_academy'))
async def about(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ABOUT_ACADEMY
    )

@router_start.message(Command('about_bot'))
async def about_bot(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Без названия.jpg"),
        caption=ABOUT_BOT
    )



