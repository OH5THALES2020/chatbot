import pandas as pd
from datetime import datetime

tidesDataFileBrest = "./hackathon_2020/data/annuaire_maree_BREST_2020.csv"


def getMaree(ville, date, pm_bm):
    print("REQUEST ville: ", ville, ", date: ", date, ", PM/BM: "+pm_bm)
    fileName = getDataFileName(ville)
    try:
        fileName
    except NameError:
        print("Ville inconue")
    else:
         return readTidesFile(fileName, date, pm_bm)

def getDataFileName(ville):
    if ville is "brest":
        return tidesDataFileBrest
    else:
        pass

def readTidesFile(fileName, date, pm_bm):
    if pm_bm is "pm":
        return searchTide(date, fileName, "Heure PM Matin", "Heure PM Soir"),
    elif pm_bm is "bm" :
        return searchTide(date, fileName, "Heure BM Matin", "Heure BM Soir")
    else:
        return "define pm/bm"

def searchTide(requestDate, fileName, heureMatinHeader, heureSoirHeader):
    print("heure system ", datetime.now().time())
    for index in range(365):
        date = pd.read_csv(fileName, sep=';')["Date"][index]
        if date == requestDate:
            print("found date ", date)
            heureMatin =  pd.read_csv(fileName, sep=';')[heureMatinHeader][index]     
            return heureMatin
        else:
            continue

if __name__=="__main__":
    print(getMaree("brest","19/01/2020","pm"))