from aiogram import types
from setup import dp


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hello, stranger 👋!\nI'm Mr. Beam!\nEnter /generate to start hacking!")
