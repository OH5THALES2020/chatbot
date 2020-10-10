'''
Created on 10 oct. 2020

@author: philippe
'''

import requests
import json

from datetime import datetime
import time

class HauteurEau:

    def __init__(self):
        self.url = "https://tides.p.rapidapi.com/tides"
        self.headers = {
            'x-rapidapi-host': "tides.p.rapidapi.com",
            'x-rapidapi-key': "8cf5631d37msh3b12568a1ccaff7p170cf0jsnaf661db4930c"
        }

    #fonction qui calcule la  hauteur d'eau
    # - a une position geographique donnee (latitude / longitude)
    # - a une date donnee
    # Unites :
    # latitude et longitude : degres
    # date (heure utc)
    # resultat donne en metres
    def calculerHauteurDeau(self,latitude,longitude,date):
            
        paramTimestamp = "{}".format(int(date.timestamp()).__str__())
        paramLatitude = "{}".format(float(latitude).__str__())
        paramLongitude = "{}".format(float(longitude).__str__())
    
        querystring = {"interval":"30","timestamp":paramTimestamp,"duration":"1440","latitude":paramLatitude,"longitude":paramLongitude}
        
        print(querystring) 

        self.response = requests.request("GET", self.url, headers=self.headers, params=querystring)

        data = self.response.json()
        
        print(type(data))

        print(data)
        hauteur = data["heights"][0]["height"]
        
        print(hauteur)
    
        return hauteur
    
    def test(self):
        
        date = datetime.utcnow()
        
        self.calculerHauteurDeau(47.44, -4.8, date)