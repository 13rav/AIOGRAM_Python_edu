from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer("Смотри какой прикольный котик \U00002764")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEFpD5jA3Qs-u_FtElq9YWD5zOM7WF7nAACLwADkp8eEZBJJAjtNPWNKQQ")

@dp.message_handler()
async def send_reverse_emoji(message: types.Message):
    if message.text=="\U00002764 ":
        await message.answer("\U0001f5a4")

if __name__ == '__main__':
    executor.start_polling(dp)
