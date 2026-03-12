import asyncio
from _pyrepl import commands
from aiogram import Bot,Dispatcher
from config import Config, load_config
from handlers.command_start import router_start
from handlers.command_backend import router_backend
from handlers.command_frontend import router_frontend
from db.engine import create_db, drop_db, session_maker
from db.db import DataBaseSession

# Функция выполняется при запуске приложения (бота / сервера)
async def on_startup():
    # Флаг для полной очистки базы данных
    # Если поставить True — все таблицы будут удалены и созданы заново
    run_param = False

    # Если включена очистка базы
    if run_param:
        await drop_db()  # удаляем все таблицы

    # Создаем таблицы базы данных, если они еще не существуют
    await create_db()

    # Сообщение в консоль о запуске сервера
    print("Сервер успешно запущен! 😊 Привет, босс!")


# Функция выполняется при остановке приложения
async def on_shutdown():
    print("Сервер остановлен. 😔 Проверьте его состояние, босс!") # Сообщение о корректном завершении работы

async def main() -> None:
    config: Config = load_config()
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router_start)
    dp.include_router(router_backend)
    dp.include_router(router_frontend)

    # Регистрируем функцию, которая выполняется при запуске бота
    # В нашем случае: создание таблиц, вывод приветствия в консоль
    dp.startup.register(on_startup)

    # Регистрируем функцию, которая выполняется при остановке бота
    # В нашем случае: вывод сообщения о завершении работы
    dp.shutdown.register(on_shutdown)

    # Подключаем middleware базы данных
    # Каждый обработчик (handler) теперь автоматически получает session в data
    # session_pool — это наша фабрика асинхронных сессий SQLAlchemy
    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
