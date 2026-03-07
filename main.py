import asyncio
from aiogram import Bot,Dispatcher
from config import Config, load_config
from handlers.command_start import router_start


async def main() -> None:
    config: Config = load_config()
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router_start)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
