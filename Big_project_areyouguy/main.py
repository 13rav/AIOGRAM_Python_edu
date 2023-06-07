from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated, Message, ChatMember
from TOKEN import TOKEN_API
from func import check_user


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


members={}
MemberId=[]
MemberUsername = ""
reg_text = """зарегестрированы следующие участники:
    """

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="введи команду /registration чтобы учавствовать в выборе")

@dp.message_handler(commands=['registration'])
async def reg_command(message: types.Message):
    member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    MemberUsername = member.user.username
    MemberId.append(member.user.id)

    text333 = check_user(message.chat.id, member.user.id, member.user.username)

    await bot.send_message(text=text333, chat_id=message.chat.id)
    print(text333)
    #await bot.send_message(text="erg "+MemberUsername+" fg "+str(MemberId), chat_id=message.chat.id)
    #await bot.send_message(text=reg_text+f'\n он @{MemberUsername} вошел в чат', chat_id=message.chat.id)
    #await bot.send_message(text=reg_text, chat_id=message.chat.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)