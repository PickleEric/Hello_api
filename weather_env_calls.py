import requests
import os
from datetime import datetime
import logging
"""
Logging is really important it helps build and maintain a program. Rather then allowing the user to see 
different things that you may need to find. Say if something changes or isnt working if you log it rather 
then print it the user can never know what you may be doing. Especially if you are logging sensative infromation
which you should log for your own reference.
"""
def main():

    city = input('What city? ')
    country = input('What country is that in? ')
    #location = get_location() # Could not get location to work for some reason. re did all locations but still errored
    #print(location)
    try:
        data = get_current_conditions(city, country)
        logging.info(data)
        if data:
            current_temp = extract_temperature(data)
            logging.info(current_temp)
            print(f'The current temperature in {city.title()}, {country.upper()} is {current_temp:.2f}F')
            date_and_time(city, country)
        else:
            print('This location was not found.')

    except Exception as e:  
        print('Sorry, there was an error fetching data. '
              'Please check your internet connection, and if that\'s ok, report this to the developer.', e)

def get_location(): # create input validation.
    city, country = '', ''
    while len(city) == 0:
        city = input('What city?')
    while len(country) != 2 or not country.isalpha():
        country = input('What is the country code?')
    location = f'{city}, {country}'
    logging.debug(location)
    return location
    

def get_current_conditions(city, country):

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    key = os.environ['WEATHER_KEY']  # Make sure you set this environment variable
    assert key is not None # raises an error if environment variable is not set


    location = '%s,%s' % (city, country)
    params = {'q': location, 'units': 'imperial', 'APPID': key}

    response = requests.get(base_url, params)

    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return None
    logging.exception(response)

    # Any other errors, raise an exception
    response.raise_for_status()  # Raise an exception if the status code is not 2xx or 3xx


def extract_temperature(data):
    return data['main']['temp']

def date_and_time(city, country):
    
    key = os.environ.get('WEATHER_KEY')  # Returns None if not found
    query = {'q': {city : country}, 'units': 'imperial', 'appid': key}
    logging.info(query)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    logging(data)
    forecast_items = data['list']

    for forecast in forecast_items:
        timestamp = forecast['dt']  # Unix timestamp
        date = datetime.fromtimestamp(timestamp)  # Convert to a datetime
        logging.info(date)
        weather = forecast['weather']
        for description in weather:
            description = description['description']
        wind = forecast['wind']['speed']
        temp = forecast['main']['temp']
        print(f'at {date} temp is {temp} the weather is like {description} wind speed: {wind}')
        

  
if __name__ == '__main__':
    logging.info('Weather env calls')
    main()