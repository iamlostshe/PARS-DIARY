'Main module to start telegram-bot'

# Integrated python modules
import asyncio
import os

# Modules need to be installed
from loguru import logger

# Aiogram
from aiogram import Bot, Dispatcher

# Writed by me modules
from handlers import routers
from utils.db import DB_NAME
from utils.load_env import TOKEN


# Starting bot
async def main() -> None:
    'Основная функция запуска бота'
    # Connecting log file
    logger.add("log.log")

    # Checking for the existence of the users.json file
    if not os.path.isfile(DB_NAME):
        # and creating if it does not exist
        with open(DB_NAME, 'a+', encoding='UTF-8') as f:
            f.write('{}')

    # Initializating dp and bot
    dp = Dispatcher()
    bot = Bot(token=TOKEN)

    # Connect hendlers
    for r in routers:
        logger.info('Include router: {} ...', r.name)
        dp.include_router(r)

    # Starting
    logger.info('Bot start polling...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
