from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from config import stay_home
from parser_weather import Parser
from buttons import user_kb
import datetime
import os


bot = Bot('5943153454:AAG5fynEBoLObp7za7MpfLpVbI8j-ObMORs')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_Message(message: types.Message):
    await message.answer('Привет, я бот который подскажет как провести день, в связи с погодой', reply_markup=user_kb)


@dp.message_handler(Text(equals='Какая сегодня погода?', ignore_case=True))
async def today(message: types.Message):
    msg = stay_home[
        list(stay_home.keys())[datetime.datetime.now().weekday()]
    ]
    await message.answer(f'{msg}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)