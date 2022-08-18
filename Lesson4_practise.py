from ast import If
from email import message
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
import string
import random


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['description'])
async def description_message(message: types.Message):
    await message.answer(text="Данный бот умеет что-то делать")

@dp.message_handler ()
async def send_random_letter(message: types.Message):
    if Message. :
        await message.answer(text="send photo")
    else:
        await message.answer(random.choice(string.ascii_letters))

if __name__ == '__main__':
    executor.start_polling(dp)

#grewa