from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



if __name__ == '__main__':
    executor.start_polling(dp)
