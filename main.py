import asyncio
from aiogram import Bot, Dispatcher, F

from handlers.handlers import router


async def main():
    bot = Bot(token='7599772296:AAFEayHf0Zm9de08s7nBQXG3LdIAjj9od_I')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finish bot')
