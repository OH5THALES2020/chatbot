import requests
import json
import datetime

from meteofrance.client import MeteoFranceClient
from meteofrance.helpers import readeable_phenomenoms_dict
class PositionLatLong:  
  latitude = 0.0
  longitude = 0.0 # list cannot be initialized here!

def getLatLongFromCityName(ville):   
    client = MeteoFranceClient()
    list_places = client.search_places(ville)
    my_place = list_places[0]

    position = PositionLatLong()
    position.latitude = my_place.latitude
    position.longitude = my_place.longitude
    
    return position
