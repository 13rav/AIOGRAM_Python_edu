from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)
async def echo(message: types.Message):
    await message.answer(text="Прислали фото")
if __name__ == '__main__':
    executor.start_polling(dp)

    #fer
