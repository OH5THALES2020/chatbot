import pandas as pd
from datetime import datetime

tidesDataFileBoulogneSurMer = "/hackathon_2020/data/annuaire_maree_BOULOGNE-SUR-MER_2020"
tidesDataFileBrest = "./hackathon_2020/data/annuaire_maree_BREST_2020.csv"
tidesDataFileLaRochelle = "./hackathon_2020/data/annuaire_maree_LA_ROCHELLE-PALLICE_2020.csv"
tidesDataFileLeHavre = "./hackathon_2020/data/annuaire_maree_LE_HAVRE_2020.csv"
tidesDataFileSaintMalo = "./hackathon_2020/data/annuaire_maree_SAINT-MALO_2020.csv"
tidesDataFileSocoa = "./hackathon_2020/data/annuaire_maree_SOCOA_2020.csv"

def getMaree(ville, date, pm_bm='pm'):
    print("REQUEST ville: ", ville, ", date: ", date, ", PM/BM: "+pm_bm)
    fileName = getDataFileName(ville)
    try:
        fileName
    except NameError:
        print("Ville inconue")
    else:
         return readTidesFile(fileName, date, pm_bm)

def getDataFileName(ville):
    if ville is 'boulogne-sur-mer':
        return tidesDataFileBoulogneSurMer
    if ville is "brest":
        return tidesDataFileBrest
    if ville is "larochelle":
        return tidesDataFileLaRochelle
    if ville is "lehavre":
        return tidesDataFileLeHavre
    if ville is "saintmalo":
        return tidesDataFileSaintMalo
    if ville is "socoa":
        return tidesDataFileSocoa
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
    print(getMaree('larochelle',"10/10/2020"))