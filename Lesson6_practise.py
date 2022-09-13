from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>показывает список комманд</em>
<b>/give</b> - <em>отправляет котика</em>"""

#@dp.message_handler()
#async def message_counter(message: types.Message):
#    await message.answer(text=str(message.text.count('⚡')))

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND , parse_mode='HTML')

@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer("Смотри какой прикольный котик \U00002764")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEFpD5jA3Qs-u_FtElq9YWD5zOM7WF7nAACLwADkp8eEZBJJAjtNPWNKQQ")
#
# @dp.message_handler()
# async def send_reverse_emoji(message: types.Message):
#    if message.text=="\U00002764 ":
#        await message.answer("\U0001f5a4") rrrr

if __name__ == '__main__':
    executor.start_polling(dp)
