import os
import requests
from pprint import pprint

def main():
    url = 'http://api.openweathermap.org/data/2.5/weather'  # Replace this with your own URL and key
    data = requests.get(url).json()
    pprint(data)
    weather_description = data['weather'][0]['description']

    temp_f = data['main']['temp']
    print(f'The weather is {weather_description}, the temperature is {temp_f:.2f}F.')

    key = os.environ.get('WEATHER_KEY')
    query= {'q': 'Minneapolis,us', 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()

if __name__ == '__main__':
    main()