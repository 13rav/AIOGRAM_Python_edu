from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

rKeyBoard = ReplyKeyboardMarkup(resize_keyboard=True)
rButton1 = KeyboardButton(text='/help')
rButton2 = KeyboardButton(text='/vote')
rKeyBoard.add(rButton1, rButton2)

if __name__ == '__main__':
    executor.start_polling(dp)
