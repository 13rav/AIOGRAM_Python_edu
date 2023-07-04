""" from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR, statistic
test_dic={"Alice":6, "Bob":1, "Green":1, "Harry":3, "Liza":5}

sorted_dic = dict(sorted(test_dic.items(), key = lambda item: item[0]))

print(sorted_dic)
for i in range(0, 1, 2):
    sorted2_dic = test_dic.items()

check_user(111, 122343244235, "andrusha")
check_user(111, 943278234, "Roma")
check_user(111, 984382899234, "Daniil")
check_user(111, 8437818234787, "Ilya")
check_user(555, 81288914, "Sanya")
check_user(555, 834895882345, "Grisha")
check_user(555, 122343244235, "andrusha")

updateDB_thePIDOR(111, 943278234, 2)
updateDB_thePIDOR(111, 943278234, 3)
updateDB_thePIDOR(111, 8437818234787, 2)
updateDB_thePIDOR(111, 8437818234787, 1)
updateDB_thePIDOR(111, 8437818234787, 2)
updateDB_thePIDOR(111, 8437818234787, 4)
updateDB_thePIDOR(111, 984382899234, 1)

print(statistic(111))
print(GlobalDB) """

from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated, Message, ChatMember, ContentType
from TOKEN import TOKEN_API
from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR, statistic
import random, datetime, asyncio
from messages import list2, list1, chose_list

random.seed(76453332234567890987654323456797654656445690087.887656567)
gifs_list = ["CgACAgIAAxkBAAN_ZKP0AsOyKhjtIGAvUCP_zZOvR90AAs4rAAJDRelLIEfsMaE_4MgvBA", "CgACAgQAAxkBAAN7ZKPrqSR2MLIoutZ55SBX4N9VKnwAAv4CAAJSXA1TGIuwur40fk4vBA", "CgACAgQAAxkBAAOBZKP0CUFQUKIxV1v-nsD0JSAUCV8AAksCAALf15VSdd8KrZlFl5kvBA"]

offset_utc = datetime.timedelta(hours=3)
tzinf = datetime.timezone(offset_utc, name="MSK")
now = datetime.datetime.now(tz=tzinf)
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

""" @dp.message_handler(content_types=ContentType.ANY)
async def fileID_command(message: types.Message):
    #await bot.send_video(message.chat.id, "CgACAgQAAxkBAAEB4hJknzHLV9QQeKZaj9fr1Mr8rQ-KnQAC_gIAAlJcDVPEJXWg1s6K6i8E", )
    await message.answer(text=str(message.document.file_unique_id)+"   "+str(message.document.file_id))
 """

#fer = [(bot.send_message), ()]

@dp.message_handler(commands="regi")
async def regi_command(message: types.Message):
   s = random.choice(chose_list)

   for i in range(len(s)//2):
       await s[i](message.chat.id, s[i+(len(s))//2])
       await asyncio.sleep(1.5)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)