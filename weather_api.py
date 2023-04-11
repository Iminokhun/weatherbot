import requests
from pprint import pprint
import datetime

# icons = {
#     '01d': '\U00002600',
#     '01n': '\U00002600',
#     '02d': '\U0001F324',
#     '02n': '\U0001F324',
#     '03d': '\U00002601',
#     '03n': '\U00002601',
#     '04d': '\U0001F325',
#     '04n': '\U0001F325',
#     '09d': '\U0001F327',
#     '09n': '\U0001F327',
#     '10d': '\U0001F327',
#     '10n': '\U0001F327',
#     '11d': '\U0001F329',
#     '11n': '\U0001F329',
#     '13d': '\U0001F328',
#     '13n': '\U0001F328',
#     '50d': '\U000026C8',
#     '50n': '\U000026C8',
# }

def get_weather(city):
    cord = city.split(';')


    KEY = '137d62f3c460fac41edca5930e84af7c'

    parameters = {
        'appid': KEY,
        'units': 'metric',
        'lang': 'ru',
        'lat': cord[0],
        'lon': cord[1],
    }
    try:
        data = requests.get(params=parameters, url=f'https://api.openweathermap.org/data/2.5/weather').json()
        temp = data['main']['temp']
        clouds = data['clouds']['all']
        humidity =data['main']['humidity']
        wind = data['wind']['speed']
        send = f'''
    Температура - <b>{temp}°C</b>
    Влажность - <b>{humidity}%</b>
    Скорость ветра - <b>{wind} м/с</b>
    Облочность - <b>{clouds}%</b>'''

        return send.strip()
    except Exception as e:
        print(e)
        send_ex = f'На запрос <b>{city}</b> ничеги не найдено'
        return send_ex

















