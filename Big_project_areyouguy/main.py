from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated, Message, ChatMember
from TOKEN import TOKEN_API
from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR
import random, datetime

offset = datetime.timedelta(hours=3)
tzinf = datetime.timezone(offset, name="MSK")
now = datetime.datetime.now(tz=tzinf)
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

    chatInGlobalDB = GlobalDB.get(message.chat.id)

    try:
        checkMembersID = bool(GlobalDB[message.chat.id]["membersID"])
    except Exception as er:
        checkMembersID = False

    if chatInGlobalDB is None:
        await bot.send_message(text="воспользуйтесь командой регистрации /registration", chat_id=message.chat.id)
        return None
    if checkMembersID == False:
        await bot.send_message(text="воспользуйтесь командой регистрации /registration", chat_id=message.chat.id)
        return None
    if GlobalDB[message.chat.id]["nowDay"] != now.strftime("%w"):
        id_nomination = random.choice(GlobalDB[message.chat.id]['membersID'])
        nowDay = now.strftime("%w")
    #GlobalDB[message.chat.id][id_nomination] = GlobalDB[message.chat.id][id_nomination]+1
        check_result01 = updateDB_thePIDOR(message.chat.id, id_nomination, nowDay)
        await bot.send_message(text="пидор дня @"+IDTOuser[id_nomination], chat_id=message.chat.id)
        return None
    
    await bot.send_message(text="пидоря дня уже номинирован. И это @"+IDTOuser[GlobalDB[message.chat.id]["id_thePIDOR"]], chat_id=message.chat.id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)