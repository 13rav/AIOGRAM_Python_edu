from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ContentTypes
import random
from TOKEN import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def resend_photo(message: types.Message):
    await bot.send_message(text=str(message.photo[0].file_id), chat_id=message.chat.id)
    await bot.send_photo(chat_id=message.chat.id, photo=str(message.photo[0].file_id))

if __name__ == '__main__':
    executor.start_polling(dp)

