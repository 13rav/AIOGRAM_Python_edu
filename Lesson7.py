from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['image'])
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://img.championat.com/news/big/j/n/durov-otkazalsja-ot-edy-i-alkogolja-poehala-krysha-ili-mozgi-vstali-na-mesto_15604007831083690418.jpg")

if __name__ == '__main__':
    executor.start_polling(dp)