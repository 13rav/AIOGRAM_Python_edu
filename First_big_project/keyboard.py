from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


rKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
Button1 = KeyboardButton(text = '/help')
Button2 = KeyboardButton(text = '/description')
Button3 = KeyboardButton(text = 'Random photo')

rKeyboard.add(Button2).add(Button1, Button3)

photoKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
phButton1 = KeyboardButton(text = 'Фото')
phButton2 = KeyboardButton(text = 'Главное меню')

photoKeyboard.add(phButton1, phButton2)