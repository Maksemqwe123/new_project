from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Какая сегодня погода?')
)
