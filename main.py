import asyncio
import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

load_dotenv()

Token = os.getenv("Token")

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(Command('aboutacademy'))
async def aboutacademy(messege: Message):
    await messege.answer_photo(
        photo=FSInputFile("photo/img_academy.jpg"),
        caption=f"""Academy — это образовательная академия, созданная для обучения и развития.
Мы помогаем студентам получать новые знания, развивать навыки и достигать своих целей в образовании и карьере."""
    )

@dp.message(Command('aboutbot'))
async def aboutbot(messege: Message):
    await messege.answer_photo(
        photo=FSInputFile("photo/robot.webp"),
        caption=f"""Это бот для регистрации на курсы.
Он помогает пользователям просматривать доступные курсы, подавать заявки и управлять своей регистрацией быстро и удобно."""
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
