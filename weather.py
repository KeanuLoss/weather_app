from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()    # loads the API-Key

def get_current_weather(city="Hamburg"):    # default value when no city was given as an input yet

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'


    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":   #if this file is called directly instead af calling a file that might call the entire application for the web then we go ahead and run this file as if it's at the terminal
    print('\n *** Get Current Weather Conditions *** \n')
    city = input("\n Please enter a City name: ")
    
    if not bool(city.strip()):
        city = "Hamburg"
        
    
    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)