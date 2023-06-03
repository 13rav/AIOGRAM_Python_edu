from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from TOKEN import TOKEN_API

is_voted = False

ikb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('🧡', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
    [InlineKeyboardButton('Close keyboard', callback_data='close')],
])

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id, photo="https://russianemirates.com/assets/thumbnails/6a/6acb61728d4b5c8f8ae2767ed5a8faa0.jpg", 
                            caption="Нравится ли тебе Пашенька Дуров?",
                            reply_markup=ikb2)
    
@dp.callback_query_handler()
async def ikb_cb(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer("Фото понравилось")
    elif callback.data == 'dislike':
        await callback.answer("Фото не понравилось")
    elif callback.data == "close":
        await bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id, 
        reply_markup=None)

if __name__ == '__main__':
    executor.start_polling(dp)
    
##доделать по видеоуроку, работа с глобальной переменной
