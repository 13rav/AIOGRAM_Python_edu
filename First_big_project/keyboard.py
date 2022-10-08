from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


rKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
Button1 = KeyboardButton(text = 'help')

rKeyboard.add(Button1)