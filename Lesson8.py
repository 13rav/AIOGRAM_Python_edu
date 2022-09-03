
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
Button1 = KeyboardButton('/sticker')
Button2 = KeyboardButton('/photo')
keybordTest = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keybordTest.add(Button1).insert(Button2)

HELP_COMMAND = """"Это тестовый бот, и он становится умнее

<b>/sticker</b> отправляет стикер чык-чырыка
<b>/photo</b> отправляет фото Пашы Дурова"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=keybordTest)

@dp.message_handler(commands=['sticker'])
async def sticker_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEFv3ljE3-1cl7bDAquCNiOLu4cc8bq9AACBAADoB7WCpwLfFk0SuWaKQQ')

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='https://img.championat.com/news/big/j/n/durov-otkazalsja-ot-edy-i-alkogolja-poehala-krysha-ili-mozgi-vstali-na-mesto_15604007831083690418.jpg')

if __name__ == '__main__':
    executor.start_polling(dp)