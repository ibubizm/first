import requests
import bot

city = 'minsk'
wather_key = '75d1edbe3e0412ef44c4d87e40409fdc'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={wather_key}'


def cityes(city):
    city = bot.get_message()
    city = city['text']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={wather_key}'
    print(city)
    return url


def get_updates():
    r = requests.get(cityes(city))
    return r.json()


def get_wather():
    data = get_updates()
    temp = data['main']['temp']
    print(temp)
    return temp
