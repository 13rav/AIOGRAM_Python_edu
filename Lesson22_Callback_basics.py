from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from TOKEN import TOKEN_API

ikb1 = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('🧡', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike'),]
])

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id, photo="https://russianemirates.com/assets/thumbnails/6a/6acb61728d4b5c8f8ae2767ed5a8faa0.jpg", 
                            caption="Нравится ли тебе Пашенька Дуров?",
                            reply_markup=ikb1)
    
@dp.callback_query_handler()
async def ikb_cb(callback: types.CallbackQuery):
    if callback.data == "dislike":
        await callback.answer(text="Фото не понравилось")
    else:
        await callback.answer(text="Вам понравился Дуров")


if __name__ == '__main__':
    executor.start_polling(dp)