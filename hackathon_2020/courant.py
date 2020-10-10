# 
# Module de mesure de courant
#
# OH5 Ocean Chatbot

# Calcule le courant a ue position latitude e longitude (en radian) donnée.
def calculer_courant(latitudeEnRadian,  longitudeEnRadian):
    result = VecteurCourant(48.338109,  4.574518,  3.6651914291880923,  5.0)
    
    return result;


# courant selon l amaree a une position lat/lon connue
class PointCourant:
    lat =""
    lon=""
    # courants vive eaux
    courantsVE = ""
    # courant mortes eaux
    courantsME=""
    
    def __init__(self,  a_lat,  a_lon,  a_courantsVE,  a_courantsME):
        self.lat = a_lat
        self.lon = a_lon
        self.courantsVE = a_courantsVE
        self.courantsME = a_courantsME

    def __str__(self):
        return self.lat +", "+self.lon +"\n"  +self.courantsVE  +  self.courantsME


# Represente le vecteur courant.
class VecteurCourant:
    azimuth = 0.0
    vitesse = 0.0
    lat=0.0
    lon=0.0
        

    def  __init__(self,  an_azimuth,  a_vitesse,  a_lat,  a_lon):
        self.azimuth = an_azimuth;
        self.vitesse = a_vitesse;
        self.lat = a_lat;
        self.lon = a_lon;
        

if __name__ == "__main__":
    import sys
    vecteur_courant = calculer_courant(int(sys.argv[1]),  int(sys.argv[2]))    
    print(vecteur_courant)
