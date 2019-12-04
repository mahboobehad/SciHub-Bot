# In the name of God
import logging

from loguru import logger
from telegram import Bot
from telegram.ext import Updater

from config import BotConfig
from state.state_machine import StateMachine

if __name__ == '__main__':
    logger.info("bot started!")
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=BotConfig.bot_token, base_url=BotConfig.base_url, base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher
    StateMachine(dispatcher).start()
    updater.start_polling(1)
