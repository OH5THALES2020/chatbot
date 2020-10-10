#-*- coding: utf-8 -*-

#Consultation API météo avec openweathermap
# API dispo ici : https://openweathermap.org/current

import requests
import json
import datetime
ville = "brest" ### TODO : a mettre en input
	
#récupère le temps actuel 
url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095&unit=standard&lang=fr"
#url="http://api.openweathermap.org/data/2.5/weather?q=Londres,uk&APPID=beb97c1ce62559bba4e81e28de8be095"

r_weather = requests.get(url_weather)
data = r_weather.json()

print(data)

lat = data['coord']['lat']
lon = data['coord']['lon']
print("Vous etes a " + ville + " Lat : " + str(lat) + " / long : " + str(lon))

#temperature moyenne
t = data['main']['temp']       
print("La temperature moyenne est de {} degres Celsius".format(t-273.15))
#écart de température
t_min = data['main']['temp_min']
t_max = data['main']['temp_max']
print("Les temperatures varient entre {}".format(t_min-273.15) + " a {} degres Celsius".format(t_max-273.15))
#taux d'humidité
humidite = data['main']['humidity']
print("Taux d'humidite de {}".format(humidite) + "%")
#état du ciel 
temps = data['weather'][0]['description']
print("Conditions climatiques : {}".format(temps))

# vent
#"wind": {
#    "speed": 1.5,
#    "deg": 350
#  },

speed = data['wind']['speed']
direction = data['wind']['deg']

print("Vent : {} meter/sec,".format(speed) + ", direction {} degrees".format(direction))


##jour = raw_input("De quel jour voulez vous la météo ?")
##date = datetime.datetime(year=2017, month=5, day= jour)
#ville = "brest"
#url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
#r_forecast = requests.get(url_forecast)
#data = r_forecast.json()
##print(data)
       
#for i in range (0,25):
#	t = data['list'][i]['main']['temp']
#	temps = data['list'][i]['weather'][0]['description']
#	time = data['list'][i]['dt_txt']
#	print("Previsions pour le {}".format(time))
#	print("La temperature moyenne est de {} degres Celsius".format(t-273.15))
#	print("Conditions climatiques : {}".format(temps))


##traduction possible d'anglais en français ? mes données sont en anglais et je les ressort en french