import requests
import datetime
from openpyxl import Workbook
from os import path

API_KEY = '73b69dd502289cfcb1322eb34935b90b'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
LANG = 'en'
FILE_EXCEL = 'data.xlsx'


def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))
    return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)




def get_weather(city_name):
    params = {
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANG,
        "q": city_name
    }
    try:
        r = requests.get(API_URL, params=params)
        return r.json()
    except:
        return {"cod": 0, "message": "Failed data access"}


def print_weather(data):

    if data['cod'] != 200:
        print(data['message'])
        return {}
    else:
        sunrise_time = get_date_time(data['sys']['sunrise'], data['timezone'])
        sunset_time = get_date_time(data['sys']['sunset'], data['timezone'])
        print(f"""
        Localization: {data['name']}, Country: {data['sys']['country']}
        Temreture: {data['main']['temp']} ℃
        Pressure: {data['main']['pressure']} Pa
        Humidity: {data['main']['humidity']}%
        Speed of wind: {data['wind']['speed']} m/sec
        Weather conditions: {data['weather'][0]['description']}
        Sunrise: {sunrise_time}
        Sunset time: {sunset_time}
        """)

        print("+" * 50)
        return data

      
print('*' * 70)
print(("""* Hi! I'll help you to know weater in every city of the world.
* Just enter request in format: city[,country_code]
* If you want to exit from program, then just press Enter"""))
print('*' * 70)

while True:
    q = input('Please enter the name of the city: ')
    if not q:
        print('See you later :)')
        break
    else:
        weather = get_weather(q)
        print("+" * 50)
        weatherer = print_weather(weather)

"""
{'coord': {'lon': -0.1257, 'lat': 51.5085}, 
'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 
'base': 'stations', 
'main': {'temp': 11.4, 'feels_like': 11.02, 'temp_min': 9.27, 'temp_max': 12.29, 'pressure': 980, 'humidity': 93}, 
'visibility': 10000, 
'wind': {'speed': 4.63, 'deg': 180}, 'rain': {'1h': 1}, 
'clouds': {'all': 100}, 'dt': 1708598371, 
'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1708585324, 'sunset': 1708622786}, 
'timezone': 0, 
'id': 2643743, 
'name': 'London', 
'cod': 200}

'country': 'BY', 'sunrise': 1708578963, 'sunset': 1708615856, 'timezone': 10800
'country': 'GR', 'sunrise': 1708578941, 'sunset': 1708618654, 'timezone': 7200
"""
# r = requests.get(API_URL, params=params)
# # res =
# print(res['sys']['country'])