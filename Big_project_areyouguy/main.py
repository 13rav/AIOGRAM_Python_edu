from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated, Message, ChatMember
from TOKEN import TOKEN_API
from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR, statistic
import random, datetime, asyncio
from messages import list2, list1, chose_list

offset_utc = datetime.timedelta(hours=3)
tzinf = datetime.timezone(offset_utc, name="MSK")
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

    text_to_send = check_user(message.chat.id, member.user.id, member.user.username)

    await bot.send_message(text=text_to_send, chat_id=message.chat.id)
    print(text_to_send)

@dp.message_handler(commands=['thePIDOR'])
async def nomination(message: types.Message):
    copy_DB = GlobalDB

    chatInGlobalDB = copy_DB.get(message.chat.id)

    try:
        checkMembersID = bool(copy_DB[message.chat.id]["membersID"])
    except Exception as er:
        checkMembersID = False

    if chatInGlobalDB is None:
        await bot.send_message(text="Воспользуйтесь командой регистрации /registration", chat_id=message.chat.id)
        return None
    if checkMembersID == False:
        await bot.send_message(text="Воспользуйтесь командой регистрации /registration", chat_id=message.chat.id)
        return None
    if copy_DB[message.chat.id]["nowDay"] != now.strftime("%w"):
        id_nomination = random.choice(copy_DB[message.chat.id]['membersID'])
        nowDay = now.strftime("%w")
    #GlobalDB[message.chat.id][id_nomination] = GlobalDB[message.chat.id][id_nomination]+1
        check_result01 = updateDB_thePIDOR(message.chat.id, id_nomination, nowDay)
        s = random.choice(chose_list)
        for i in range(len(s)//2):
            await s[i](message.chat.id, s[i+(len(s))//2])
            await asyncio.sleep(1.5)
        await bot.send_message(text="<b>Пидор дня @</b>"+IDTOuser[id_nomination], chat_id=message.chat.id, parse_mode='HTML')
        return None
    
    await bot.send_message(text="PIDOR дня уже номинирован. И это @"+IDTOuser[copy_DB[message.chat.id]["id_thePIDOR"]], chat_id=message.chat.id)


@dp.message_handler(commands=['stats'])
async def stat_func(message: types.Message):
    await bot.send_message(text=statistic(message.chat.id), chat_id=message.chat.id, parse_mode='HTML')

@dp.message_handler(commands=['info'])
async def stat_func(message: types.Message):
    await bot.send_message(text="""
/thePIDOR - Запускает спецоперацию по поиску пидора
/registratin - Зарегаться в участники
/stats - Топ 10 пидоров""", chat_id=message.chat.id)
    
@dp.message_handler(commands="backcode013")
async def backup_func(message: types.Message):
    copy_DB = GlobalDB

    for key in copy_DB:
        backup_DB = copy_DB[key]
        await bot.send_message(chat_id=117674813, text=str(backup_DB))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)