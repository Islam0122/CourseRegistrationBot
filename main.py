import asyncio
from aiogram import Bot,Dispatcher
from config import Config, load_config
from handlers.command_group import router_group_user
from handlers.command_start import router_start
from handlers.command_backend import router_backend
from handlers.command_frontend import router_frontend
from handlers.command_registration import router_registration
from handlers.command_edit import router_edit
from handlers.command_admin import router_admin
from db.engine import create_db, drop_db, session_maker
from db.db import DataBaseSession

async def on_startup():
    run_param = False

    if run_param:
        await drop_db()

    await create_db()

    print("Сервер успешно запущен! 😊 Привет, босс!")


async def on_shutdown():
    print("Сервер остановлен. 😔 Проверьте его состояние, босс!")

async def main() -> None:
    config: Config = load_config()
    admin = [6719974813]
    bot = Bot(token=config.bot.token)
    bot.my_admin_list = admin
    dp = Dispatcher()

    dp.include_router(router_start)
    dp.include_router(router_backend)
    dp.include_router(router_frontend)
    dp.include_router(router_registration)
    dp.include_router(router_edit)
    dp.include_router(router_admin)
    dp.include_router(router_group_user)

    dp.startup.register(on_startup)

    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
