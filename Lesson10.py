from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
from TOKEN import TOKEN_API

HELP_COMMAND = """"Это тестовый бот, и он становится умнее

<b>/sticker</b> отправляет стикер чык-чырыка
<b>/photo</b> отправляет фото Паши Дурова
<b>/location</b> отправляет случайную точку на карте"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
rKeyBoard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
Button1 = KeyboardButton(text='/links')
rKeyBoard.add(Button1)
iKeyBoard = InlineKeyboardMarkup(row_width=2)
iButton1 = InlineKeyboardButton(text='Google', url='https://www.google.com')
iButton2 = InlineKeyboardButton(text='Yandex', url='https://www.yandex.ru')
iKeyBoard.add(iButton1).add(iButton2)

@dp.message_handler(commands=['start'])
async def sendKeyBoard(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text = 'Hello World', reply_markup=rKeyBoard)

@dp.message_handler(commands=['links'])
async def InlineSend(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Links', reply_markup=iKeyBoard)
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp)

