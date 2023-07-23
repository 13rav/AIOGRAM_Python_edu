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
    await bot.send_message(chat_id=message.chat.id, text=str("""Топ 10 пидоров:<pre>

        <b>nikitas21</b>  --    13
        <b>vvvr1g</b>     --    12
        <b>rav_pr</b>      --    9
        <b>occult_fox</b>  --    9
        <b>Danil5621</b>   --    8
        <b>yell0wlamp</b>  --    7
        <b>dimchis3</b>    --    7
        <b>nihaoh</b>      --    5</pre>"""), parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp)

