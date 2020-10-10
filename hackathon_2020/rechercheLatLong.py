import requests
import json
import datetime

def getLatLongFromCityName(ville):   
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095&unit=standard&lang=fr"
    data = requests.get(url_weather).json()

    position =[data['coord']['lat'], data['coord']['lon']]
    return position