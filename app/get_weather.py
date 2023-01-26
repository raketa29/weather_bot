import requests
import json
import datetime
from auth.config import open_weather_api


class RusWeather:
    def __init__(self, city):
        self.city = city
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={open_weather_api}&units=metric&lang=ru"
        self.result = requests.get(self.url).json()
        self.description = self.result["weather"][0]["description"]
        self.temp = self.result['main']['temp']
        self.feels_like = self.result['main']['feels_like']
        self.pressure = self.result['main']['pressure']
        self.humidity = self.result['main']['humidity']  # Влажность
        self.wind = self.result['wind']['speed']
        self.country = self.result['sys']['country']
        self.sunrise = datetime.datetime.fromtimestamp(self.result['sys']['sunrise'])
        self.sunset = datetime.datetime.fromtimestamp(self.result['sys']['sunset'])
        self.length_of_the_day = datetime.datetime.fromtimestamp(self.result['sys']['sunset']) - datetime.datetime.fromtimestamp(self.result['sys']['sunrise'])
        self.name_city = self.result['name']
        self.weather_info_str = f'<b>⏰ {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} ⏰</b>\n' \
                                f'Погода в городе <b>🏙 {self.name_city}, {self.country}</b> \n' \
                                f'Температура <b>🌡 {self.temp}C°</b>, ощущается на <b>🌡 {self.feels_like}C°</b> \n' \
                                f'Влажность:<b>💧 {self.humidity}%</b>\nДавление:<b>💨 {self.pressure} мм.рт.ст</b>\nВетер:<b>🌬 {self.wind} м/с</b>\n' \
                                f'Восход солнца:<b>🌅 {self.sunrise}</b>\nЗакат солнца:<b>🌄 {self.sunset}</b>\n' \
                                f'Продолжительность дня:<b>🌞🕛🌛 {self.length_of_the_day}</b>\n' \
                                f'<b>Хорошего дня и помните у природы нет плохой погоды 😋</b>'


