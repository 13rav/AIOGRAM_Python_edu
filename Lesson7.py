from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['image'])
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://img.championat.com/news/big/j/n/durov-otkazalsja-ot-edy-i-alkogolja-poehala-krysha-ili-mozgi-vstali-na-mesto_15604007831083690418.jpg")

if __name__ == '__main__':
    executor.start_polling(dp)