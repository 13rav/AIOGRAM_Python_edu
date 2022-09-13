from email.message import Message
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
from Lesson5 import send_message
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

rKeyBoard = ReplyKeyboardMarkup(resize_keyboard=True)
rButton1 = KeyboardButton(text='/help')
rButton2 = KeyboardButton(text='/vote')
rKeyBoard.add(rButton1, rButton2)

iKeyBoard = InlineKeyboardMarkup(row_width=2)
iButton1 = InlineKeyboardButton(text='ДА', callback_data='Like')
iButton2 = InlineKeyboardButton(text='НЕТ', callback_data='Dislike')
iKeyBoard.add(iButton1, iButton2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello. This is smail bot', 
                            reply_markup=rKeyBoard)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, 
                            sticker='CAACAgIAAxkBAAEFv3ljE3-1cl7bDAquCNiOLu4cc8bq9AACBAADoB7WCpwLfFk0SuWaKQQ')
    await bot.send_message(chat_id=message.chat.id, 
                            text='Вам нравится данный стикер?', 
                            reply_markup=iKeyBoard)

@dp.callback_query_handler()
async def callback_work(callback: types.CallbackQuery):
    c = callback.from_user.username
    if callback.data == 'Like':
       await callback.answer()
       await bot.send_message(chat_id=callback.message.chat.id, text = f"@{c} Поставил ЛАЙК")
    else:
        await callback.answer()
        await bot.send_message(chat_id=callback.message.chat.id, text = f"@{c} Поставил ДИЗЛАЙК")


if __name__ == '__main__':
    executor.start_polling(dp)
