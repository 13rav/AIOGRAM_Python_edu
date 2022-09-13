from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text = message.text.upper())
if __name__ == '__main__':
    executor.start_polling(dp)
