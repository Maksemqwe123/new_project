from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from buttons import user_kb
import datetime
from bs4 import BeautifulSoup
import requests
import time
import os

"""Cоздание пустых переменных"""
day_of_the_week = []
number_day = []
temp_1 = []
temp_2 = []
precipitation = []
# wind = []
urls = []

"""Cоздание парсера"""


class Parser:
    def __init__(self):
        self.day_of_the_week = day_of_the_week
        self.number_day = number_day
        self.temp_1 = temp_1
        self.temp_2 = temp_2
        self.precipitation = precipitation
        # self.wind = wind
        self.urls = urls

        self._get_html()

    def _get_html(self):
        url = f'https://yandex.by/pogoda/gomel?via=moc&lat=52.42416&lon=31.014272'
        response = requests.get(url=url)

        try:
            assert response.status_code == 200
            html_source = response.text
            self._get_info(html_source)
        except AssertionError as e:
            print(f'ERROR:{repr(e)}')
            print(response.status_code)

    def _get_info(self, html_source):
        pages_info = BeautifulSoup(html_source, 'html.parser')

        day_of_the_weeks = pages_info.find_all('div', class_='forecast-briefly__name')
        for day in day_of_the_weeks:
            self.day_of_the_week.append(day.text)

        number_days = pages_info.find_all('time', class_='time forecast-briefly__date')
        for number in number_days:
            self.number_day.append(number.text)

        temps_1 = pages_info.find_all('span', class_='temp__value temp__value_with-unit')
        for temp in temps_1:
            self.temp_1.append(temp.text.replace('<_moz_generated_content_after>°</_moz_generated_content_after>', ' '))

        temps_2 = pages_info.find_all('span', class_='temp__value temp__value_with-unit')
        for temp_night in temps_2:
            self.temp_2.append(temp_night.text.replace('<_moz_generated_content_after>°</_moz_generated_content_after>', ' '))

        precipitations = pages_info.find_all('div', class_='forecast-briefly__condition')
        for pre in precipitations:
            self.precipitation.append(pre.text)

        # winds = pages_info.find_all('span', class_='wind-speed')
        # for wind_1 in winds:
        #     self.wind.append(wind_1.text)


"""Coздание бота"""
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_Message(message: types.Message):
    await message.answer('Привет, я бот который подскажет как провести день, в связи с погодой', reply_markup=user_kb)


@dp.message_handler(Text(equals='Какая сегодня погода?', ignore_case=True))
async def today(message: types.Message):
    await message.answer(f'Cегодня: {number_day[:2]}, Температура днём: {temp_1[:2]}, Температура Ночью: {temp_2[:2]}, Ожидается: {precipitation[:2]}')


if __name__ == '__main__':
    parse = Parser()
    all_info = list(zip(day_of_the_week, number_day, temp_1, temp_2, precipitation))
    for i in all_info:
        print(
            f'\n\nДень недели: {i[0]}, Число недели: {i[1]}, Teмпература Днём: {i[2]}, Температура Ночью: {i[3]}, Oжидается: {i[4]}\n\n')
    executor.start_polling(dp, skip_updates=True)
