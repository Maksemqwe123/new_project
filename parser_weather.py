from bs4 import BeautifulSoup
import requests
import time


day_of_the_week = []
number_day = []
temp_1 = []
temp_2 = []
precipitation = []
# wind = []
urls = []


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


if __name__ == '__main__':
    parse = Parser()
    all_info = list(zip(day_of_the_week, number_day, temp_1, temp_2, precipitation))
    for i in all_info:
        # with open('users_data.py', 'w+') as users_file:
        # name = {users_file.write(f'День: {day_of_the_week}\n Число недели: {number_day}\n Teмпература Днём: {temp_1}\n Температура Ночью: {temp_2}\n Oжидается: {precipitation}')}
        # for day_of_the_week, number_day, temp_1, temp_2, precipitation():
        print(f'\n\nДень недели: {i[0]}, Число недели: {i[1]}, Teмпература Днём: {i[2]}, Температура Ночью: {i[3]}, Oжидается: {i[4]}\n\n')
    # end_time = time.time() - start_time
    # print(f'\nВремя работы: {end_time} секунд')
