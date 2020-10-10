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

import rechercheLatLong

def getConditionCielCourant(ville):
   latLong = rechercheLatLong.getLatLongFromCityName(ville)
   return getConditionCielLatLon(latLong.latitude, latLong.longitude)

def getConditionCielLatLon(lat, lon) :
    url_weather = "http://api.openweathermap.org/data/2.5/weather?lat="+ str(lat) +"&lon=" + str(lon) +"&APPID=beb97c1ce62559bba4e81e28de8be095&unit=standard&lang=fr"
    r_weather = requests.get(url_weather)
    data = r_weather.json()
    temps = data['weather'][0]['description']
    return "Conditions climatiques : {}".format(temps)

def getPluieDansLheure(ville):    
    my_place = rechercheLatLong.getLatLongFromCityName(ville)
    return getPluieDansLheureLatLon(my_place.latitude, my_place.longitude)

def getPluieDansLheureLatLon(lat, lon) :
    # Init client
    client = MeteoFranceClient()

    # Search a location from name.

    # Fetch weather forecast for the location
    my_place_weather_forecast = client.get_forecast(lat, lon)

    # Get the daily forecast
    my_place_daily_forecast = my_place_weather_forecast.daily_forecast

    # If rain in the hour forecast is available, get it.
    print (my_place_weather_forecast.position["rain_product_available"] )

    if my_place_weather_forecast.position["rain_product_available"] == 1:
        my_place_rain_forecast = client.get_rain(lat, lon)
        next_rain_dt = my_place_rain_forecast.next_rain_date_locale()
        if not next_rain_dt:
            rain_status = "Pas de pluie prévu dans l'heure"
        else:
            rain_status = next_rain_dt.strftime("%H:%M")
    else:
        rain_status = "Absence de données."

    return rain_status
