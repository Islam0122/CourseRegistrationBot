from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from handlers.command_function import get_data_backend, get_data_frontend
from keyboards.command_inline import keyboard_back

parser_admin = Router()

@parser_admin.message(Command("info_backend"))
async def info_command(message: Message):
    a = get_data_backend()
    for i in a:
        await message.answer(
            i["text"],
            reply_markup=keyboard_back
        )

@parser_admin.message(Command("info_frontend"))
async def info_frontend_command(message: Message):
    a = get_data_frontend()
    for i in a:
        await message.answer(
            i["text"],
            reply_markup=keyboard_back
        )
