from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def send_message(message: types.Message):
    await message.answer('<span class="tg-spoiler">message under spoiler</span>', parse_mode="HTML")

@dp.message_handler(commands=['emoji'])
async def send_emoji(message: types.Message):
    await message.answer("send moon emoji \U0001F31A")

if __name__ == '__main__':
    executor.start_polling(dp)
