from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import random


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

HELP_COMMAND = """"Это тестовый бот, и он становится умнее

<b>/sticker</b> отправляет стикер чык-чырыка
<b>/photo</b> отправляет фото Паши Дурова
<b>/location</b> отправляет случайную точку на карте"""

Button1 = KeyboardButton('/sticker')
Button2 = KeyboardButton('/photo')
Button3 = KeyboardButton('/location')

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(Button1).insert(Button2)
kb.add(Button3)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)

@dp.message_handler(commands=['location'])
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, latitude=random.randrange(0, 76), longitude=random.randrange(0, 75))

@dp.message_handler(commands=['sticker'])
async def sticker_command(message: types.Message):
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEFv3ljE3-1cl7bDAquCNiOLu4cc8bq9AACBAADoB7WCpwLfFk0SuWaKQQ')

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://img.championat.com/news/big/j/n/durov-otkazalsja-ot-edy-i-alkogolja-poehala-krysha-ili-mozgi-vstali-na-mesto_15604007831083690418.jpg')


if __name__ == '__main__':
    executor.start_polling(dp)