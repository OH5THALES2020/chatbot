'''
Created on 10 oct. 2020

@author: philippe
'''

import requests

from datetime import datetime

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
    # resultat : un dictionnaire avec un clef hauteur (courante) en metres, une clef duree en heures une clef amplitude en metres sur les 12  prochaines heures
    def calculerHauteurDeau(self,latitude,longitude,date):
            
        paramTimestamp = "{}".format(int(date.timestamp()).__str__())
        paramLatitude = "{}".format(float(latitude).__str__())
        paramLongitude = "{}".format(float(longitude).__str__())
    
        querystring = {"interval":"60","timestamp":paramTimestamp,"duration":"1440","latitude":paramLatitude,"longitude":paramLongitude}
        
        print(querystring) 

        self.response = requests.request("GET", self.url, headers=self.headers, params=querystring)

        data = self.response.json()
        
        self.hauteur = data["heights"][0]["height"] + 3.70
        
        i = 0
        dureeMontee = 0
        hmin = self.hauteur -3.70
        hmax = self.hauteur -3.70
        
        while(i<len(data["heights"]) and (i<12)):
            
            if(data["heights"][i]["height"]>hmax):
                hmax = data["heights"][i]["height"]
                dureeMontee = dureeMontee +1
                
            if(data["heights"][i]["height"]<hmin):
                hmin = data["heights"][i]["height"]
        
            i = i+1
        
        self.amplitude = hmax - self.hauteur + 3.70
        
        resultat = {"hauteur" : self.hauteur, "duree" : dureeMontee, "amplitude" : self.amplitude}
        
        return resultat
    
    def test(self):
        
        date = datetime.utcnow()
        
        self.calculerHauteurDeau(48.03, -4.55, date)
