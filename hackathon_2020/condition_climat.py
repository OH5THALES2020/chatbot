'''
Created on 10 oct. 2020

@author: mick
'''


#Consultation API météo avec openweathermap ou meteofrance
# API openweathermap dispo ici : https://openweathermap.org/current

import requests
import json
import datetime
from datetime import datetime

from meteofrance.client import MeteoFranceClient
from meteofrance.helpers import readeable_phenomenoms_dict
from meteofrance.model import Forecast

import rechercheLatLong
import locale
locale.setlocale(locale.LC_TIME,'fr_FR.UTF-8')

def getConditionCielCourant(ville):
   latLong = rechercheLatLong.getLatLongFromCityName(ville)
   return getConditionCielLatLon(latLong.latitude, latLong.longitude)

def getConditionCielLatLon(lat, lon) :
    url_weather = "http://api.openweathermap.org/data/2.5/weather?lat="+ str(lat) +"&lon=" + str(lon) +"&APPID=beb97c1ce62559bba4e81e28de8be095&unit=standard&lang=fr"
    r_weather = requests.get(url_weather)
    data = r_weather.json()
    temps = data['weather'][0]['description']
    return "Ciel {}".format(temps)

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


def getWind(ville):    
    client = MeteoFranceClient()
    
    my_place = rechercheLatLong.getLatLongFromCityName(ville)
    jsonObj = client.get_forecast(my_place.latitude, my_place.longitude)

    premier= jsonObj.forecast[12]
    test = premier['wind']
    dt = premier['dt']
    time = datetime.utcfromtimestamp(dt).strftime('%d-%m-%Y %H:%M:%S')
    
    return ("la vitesse du vent à " + str(time) + " est de " + str(test['speed']*3600/1000) +" km/h avec une direction de " + str(test['direction']) + " degrée")


def getMeteoMarine(ville):
    client = MeteoFranceClient()
    list_places = client.search_places(ville)
    my_place = list_places[0]
    url_weather = "http://ws.meteofrance.com/ws//getDetail/france/"+ str(my_place.insee) + "0.json"
    
    #url_weather = "http://ws.meteofrance.com/ws//getDetail/france/290190.json"
    
    print (url_weather)
    
    r_weather = requests.get(url_weather)
    data = r_weather.json()
    result =data['result'] 

    res_Ville = result['ville']

    nomVille = res_Ville['nom']
    bulletinCote = res_Ville['bulletinCote']
    print(str(nomVille) + "/" + str(bulletinCote))

    # print(result)
    resume_today = result['resumes']['0_resume']
    #print(resume_today)
    
    descr = resume_today["description"]
    print (descr)

    returnedStr = ""
    if (bulletinCote == False):
        returnedStr = "Je ne trouve pas de bulletin cotier pour '"+nomVille + "'. "
    elif (bulletinCote == True):
        returnedStr = returnedStr + "Bulletin cotier de '"+nomVille + "', "
    
            
        date = int(resume_today['date'])

        #timestamp = 1602354456
        #dt_object = datetime.fromtimestamp(timestamp)
        #print("dt_object =", dt_object)

        tutu = datetime.fromtimestamp((date/1000)) #gros hack...

        heure = int(tutu.strftime("%H"))

        if (bulletinCote == True):
            if heure >= 22 :
                returnedStr = returnedStr + " Nuit. "
            elif heure >= 18:
                returnedStr = returnedStr + " Soir. "
            elif heure >= 12:
                returnedStr = returnedStr + " Après-midi. "
            else:
                returnedStr = returnedStr + " Matin. "

        dateStr = tutu.strftime("%A %e %B")
        print (dateStr)
        returnedStr = returnedStr + "Prévisions pour la journée du " + dateStr +" ."
        
        ventForce = int(resume_today['vitesseVent'])    
        forceRafales = int(resume_today['forceRafales'])
        directionVent = int(resume_today['directionVent'])

        if (directionVent > 315) :
            directionVentStr = " Nord Nord Ouest"
        elif (directionVent == 315) :
            directionVentStr = " Nord Ouest"
        elif (directionVent > 270) :
            directionVentStr = " Nord Ouest"
        elif (directionVent == 270) :
            directionVentStr = " Ouest"
        elif (directionVent > 225) :
            directionVentStr = " Ouest Sud Ouest"
        elif (directionVent == 225) :
            directionVentStr = " Sud Ouest"
        elif (directionVent > 180) :
            directionVentStr = " Sud Sud Ouest"
        elif (directionVent == 180) :
            directionVentStr = " Sud"
        elif (directionVent > 135) :
            directionVentStr = " Sud Sud Est"
        elif (directionVent == 135) :
            directionVentStr = " Sud Est"
        elif (directionVent > 90) :
            directionVentStr = " Est Sud Est"
        elif (directionVent == 90) :
            directionVentStr = " Est"
        elif (directionVent > 45) :
            directionVentStr = " Est Nord Est"
        elif (directionVent == 45) :
            directionVentStr = " Nord Est"
        elif (directionVent > 0 ) :
            directionVentStr = " Nord Nord Est"
        elif (directionVent == 0 ) :
            directionVentStr = " Nord"

        returnedStr = returnedStr + " VENT, direction " + directionVentStr + " de " + str(ventForce) + " km/h "
        if (forceRafales > 0) :
            returnedStr = returnedStr + " avec des rafales à " + str(forceRafales) + " km/h."
        

        #" VENT : Nord-Ouest 4 à 5, fraichissant 5 à 6 en Manche l'après-midi.  #TODO
        # MER : agitée. HOULE : Ouest à Nord-Ouest 2 m sur pointe Bretagne.  #TODO
        # TEMPS : Ciel nuageux..
        returnedStr = returnedStr + ". " + getConditionCielCourant(nomVille)

        probaPluie = resume_today['probaPluie']
        print (probaPluie)
        
        if (probaPluie is int and probaPluie > 0) :
            returnedStr = returnedStr + " avec probabilité de pluie de " + str(probaPluie) + "%."
        # VISIBILITE : Bonne."

        
    print (returnedStr)
    return returnedStr
