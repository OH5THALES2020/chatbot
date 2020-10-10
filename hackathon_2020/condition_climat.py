'''
Created on 10 oct. 2020

@author: mick
'''


#Consultation API météo avec openweathermap
# API dispo ici : https://openweathermap.org/current

import requests
import json
import datetime

from meteofrance.client import MeteoFranceClient
from meteofrance.helpers import readeable_phenomenoms_dict

#fonction qui retourne les conditions climatique actuelle
def getConditionCielCourant(ville):
            
    #récupère le temps actuel 
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095&unit=standard&lang=fr"
  
    r_weather = requests.get(url_weather)
    data = r_weather.json()

    #état du ciel 
    temps = data['weather'][0]['description']
    return "Conditions climatiques : {}".format(temps)

def getPluieDansLheure(ville):
    # Init client
    client = MeteoFranceClient()

    # Search a location from name.
    list_places = client.search_places(ville)
    my_place = list_places[0]

    # Fetch weather forecast for the location
    my_place_weather_forecast = client.get_forecast_for_place(my_place)

    # Get the daily forecast
    my_place_daily_forecast = my_place_weather_forecast.daily_forecast

    # If rain in the hour forecast is available, get it.
    if my_place_weather_forecast.position["rain_product_available"] == 1:
        my_place_rain_forecast = client.get_rain(my_place.latitude, my_place.longitude)
        next_rain_dt = my_place_rain_forecast.next_rain_date_locale()
        if not next_rain_dt:
            rain_status = "Pas de pluie prévu dans l'heure à " + ville
        else:
            rain_status = next_rain_dt.strftime("%H:%M")
    else:
        rain_status = "Absence de données."

    return rain_status
