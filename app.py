from aiogram import executor
from setup import dp
import keyboards
import handlers
import services


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
