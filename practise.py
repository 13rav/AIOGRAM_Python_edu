from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from TOKEN import TOKEN_API

ikb1 = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('e', callback_data='like'), InlineKeyboardButton('qwe', callback_data='dislike'),]
])

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id, text='Hello. This is smail bot', 
                            reply_markup=rKeyBoard)

if __name__ == '__main__':
    executor.start_polling(dp)