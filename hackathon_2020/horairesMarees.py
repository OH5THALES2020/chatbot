import pandas as pd
from datetime import datetime
import math

tidesDataFileBoulogneSurMer = "./hackathon_2020/data/annuaire_maree_BOULOGNE-SUR-MER_2020.csv"
tidesDataFileBrest = "./hackathon_2020/data/annuaire_maree_BREST_2020.csv"
tidesDataFileLaRochelle = "./hackathon_2020/data/annuaire_maree_LA_ROCHELLE-PALLICE_2020.csv"
tidesDataFileLeHavre = "./hackathon_2020/data/annuaire_maree_LE_HAVRE_2020.csv"
tidesDataFileSaintMalo = "./hackathon_2020/data/annuaire_maree_SAINT-MALO_2020.csv"
tidesDataFileSocoa = "./hackathon_2020/data/annuaire_maree_SOCOA_2020.csv"

def getMaree(ville, date, pm_bm='pm'):
    print("REQUEST horaire pour ville: ", ville, ", date: ", date, ", PM/BM: "+pm_bm)
    fileName = getDataFileName(ville)
    try:
        fileName
    except NameError:
        print("Ville inconue")
    else:
        horaire = readTidesFileHoraire(fileName, date, pm_bm)
        heure_list = horaire[0].split(':')
        result = heure_list[0] + 'h'+ heure_list[1] 
        return result

def getCoef(ville, date):
    print("REQUEST coef pour ville: ", ville, ", date: ", date)
    fileName = getDataFileName(ville)
    try:
        fileName
    except NameError:
        print("Ville inconue")
    else: 
        return round(readTidesFileCoef(fileName, date))

def getDataFileName(ville):
    if ville == 'Boulogne-Sur-Mer':
        return tidesDataFileBoulogneSurMer
    if ville == "Brest":
        return tidesDataFileBrest
    if ville == "La Rochelle":
        return tidesDataFileLaRochelle
    if ville == "Le Havre":
        return tidesDataFileLeHavre
    if ville == "Saint-Malo":
        return tidesDataFileSaintMalo
    if ville == "Socoa":
        return tidesDataFileSocoa
    else:
        pass

def readTidesFileHoraire(fileName, date, pm_bm):
    if pm_bm is "pm":
        return searchTide(date, fileName, "Heure PM Matin", "Heure PM Soir"),
    elif pm_bm is "bm" :
        return searchTide(date, fileName, "Heure BM Matin", "Heure BM Soir")
    else:
        return "define pm/bm"

def readTidesFileCoef(fileName, date):
        return searchTideCoef(date, fileName, "Coeff. Maree Matin","Coeff. Maree Soir")

def searchTide(requestDate, fileName, matinHeader, soirHeader):
    #print("heure system ", datetime.now().time()) TODO
    for index in range(365):
        date = pd.read_csv(fileName, sep=';')["Date"][index]
        if date == requestDate:
            value =  pd.read_csv(fileName, sep=';')[soirHeader][index]
            #test si une seule maree dans la journee, si non on prends la suivante
            if isinstance(value,str) and len(value.strip()) == 0:
                value = pd.read_csv(fileName, sep=';')[matinHeader][index+1]
            return value
        else:
            continue
        
def searchTideCoef(requestDate, fileName, matinHeader, soirHeader):
    for index in range(365):
        date = pd.read_csv(fileName, sep=';')["Date"][index]
        if date == requestDate:
            value =  pd.read_csv(fileName, sep=';')[soirHeader][index]
            #test validitée coef
            f = float(value)
            if math.isnan(f):
                value = pd.read_csv(fileName, sep=';')[matinHeader][index+1]
            return value
        else:
            continue

if __name__=="__main__":
    print(getMaree('Saint-Malo',"11/10/2020"))
    print(getCoef('Saint-Malo',"11/10/2020"))