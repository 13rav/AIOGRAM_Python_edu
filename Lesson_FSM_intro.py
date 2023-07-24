from aiogram import executor, Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from TOKEN import TOKEN_API
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

storage_FSM = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot, storage=storage_FSM)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb1.add(KeyboardButton('Start work'))
kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2.add(KeyboardButton('/cancel'))

class ChatStates(StatesGroup):
    photo = State()
    descr = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Добро пожаловать", reply_markup=kb1)

@dp.message_handler(commands=['cancel'], state='*')
async def cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    await message.reply(text='Создание анкеты отменено', reply_markup=kb1)
    if current_state is None:
        return None
    
    await state.finish()

@dp.message_handler(Text(equals='Start work', ignore_case=True))
async def start_work(message: types.Message):
    await ChatStates.photo.set()
    await message.answer(text='Сначала отправь нам фотографию', reply_markup=kb2)

@dp.message_handler(state=ChatStates.descr)
async def description_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['descr'] = message.text

    print("Ваша фотка "+str(data['photo']+ " Ваше описание - "+str(data['descr'])))
    await message.reply(text='Ваше описание сохранено', reply_markup=kb1)
    await state.finish()

@dp.message_handler(lambda message: not message.photo, state=ChatStates.photo)
async def check_photo(message: types.Message):
    await message.answer(text="Вы загрузили не фотографию")

@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ChatStates.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await ChatStates.next()
    await message.reply(text="А теперь отправь нам описание к анкете")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

