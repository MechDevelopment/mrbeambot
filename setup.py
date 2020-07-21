import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
MRBEAM_API = "https://mrbeam-api.herokuapp.com/generate"

bot = Bot(BOT_TOKEN, parse_mode="HTML")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

logging.basicConfig(level=logging.INFO)
