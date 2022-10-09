from ast import main
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random
from aiogram.utils.exceptions import InvalidHTTPUrlContent

from TOKEN import TOKEN_API
from keyboard import rKeyboard, photoKeyboard


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """Этот знает три команды
/help         - показывает список комманд
/description  - показывает описание бота
Random photo  - отправляет случайное фото"""


@dp.message_handler(Text(equals='Random photo'))
async def RandomPhotoCommand (message: types.Message):
    await message.answer(text=str(message.from_user.id))
    await message.answer(text="Нажми <u><b>Фото</b></u> и бот пришлет тебе рандомное фото", 
                        parse_mode='HTML', reply_markup=photoKeyboard)
    await message.delete()

@dp.message_handler(Text(equals='Фото'))
async def PhotoSendCommand (message: types.Message):
    try:
        await bot.send_photo(chat_id=message.chat.id, photo=f'https://avatarko.ru/kartinka/{random.randrange(1, 6000)}/download_image')
    except InvalidHTTPUrlContent:
            
        await bot.send_message(chat_id=message.chat.id, text="Сгенерировалась битая ссылка, попробуйте еще раз")


@dp.message_handler(Text(equals='Главное меню'))
async def MainMenuCommand (message: types.Message):
    await message.answer(text="Вы в главном меню", reply_markup=rKeyboard)
    await message.delete()

@dp.message_handler(commands=['start'])
async def startCommand (message: types.Message):
    await message.answer(text='Answer', reply_markup=rKeyboard)
    await message.delete()

@dp.message_handler(commands=['help'])
async def helpCommand (message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['description'])
async def descriptionCommand (message: types.Message):
    await message.answer(text="Это маленький бот, который отправляет фото")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)