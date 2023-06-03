from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from TOKEN import TOKEN_API

is_voted = False

ikb2 = InlineKeyboardMarkup([
    [InlineKeyboardButton('🧡', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
    [InlineKeyboardButton('Close keyboard', callback_data='close')],
])

Bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id, photo="https://russianemirates.com/assets/thumbnails/6a/6acb61728d4b5c8f8ae2767ed5a8faa0.jpg", 
                            caption="Нравится ли тебе Пашенька Дуров?",
                            reply_markup=ikb2)

if __name__ == '__main__':
    executor.start_polling(dp)
    
##few dew
