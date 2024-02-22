import requests
import datetime
from openpyxl import Workbook
from os import path

API_KEY = '73b69dd502289cfcb1322eb34935b90b'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
LANG = 'en'
FILE_EXCEL = 'data.xlsx'

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
        print(weather)

# r = requests.get(API_URL, params=params)
# # res =
# print(res['sys']['country'])