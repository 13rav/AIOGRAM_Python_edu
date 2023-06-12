from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated, Message, ChatMember
from TOKEN import TOKEN_API
from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR
import random, datetime

offset = datetime.timedelta(hours=3)
tzinf = datetime.timezone(offset, name="MSK")
now = datetime.datetime.now(tz=tzinf)
nowday = None
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

reg_text = """зарегестрированы следующие участники:
    """

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="введи команду /registration чтобы учавствовать в выборе")

@dp.message_handler(commands=['registration'])
async def reg_command(message: types.Message):
    member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

    text333 = check_user(message.chat.id, member.user.id, member.user.username)

    await bot.send_message(text=text333, chat_id=message.chat.id)
    print(text333)

@dp.message_handler(commands=['thePIDOR'])
async def nomination(message: types.Message):
    global GlobalDB
    global nowday
    #member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if nowday != now.strftime("%w") and GlobalDB[message.chat.id]["todayNomination"]:
        id_nomination = random.choice(GlobalDB[message.chat.id]['membersID'])
        nowday = now.strftime("%w")
    #GlobalDB[message.chat.id][id_nomination] = GlobalDB[message.chat.id][id_nomination]+1
        check_result01 = updateDB_thePIDOR(message.chat.id, id_nomination)
        await bot.send_message(text="пидор дня @"+IDTOuser[id_nomination], chat_id=message.chat.id)
    
    await bot.send_message(text="пидоря дня уже номинирован", )



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)