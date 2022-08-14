from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    sr = message.text + " автор"
    await message.answer(text=sr)
if __name__ == '__main__':
    executor.start_polling(dp)

    #fs
