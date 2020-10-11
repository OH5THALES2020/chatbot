# -*- coding: utf-8 -*-

from flask import Flask, request
import json
from datetime import datetime
import condition_climat
from horairesMarees import *
from HauteurEau import HauteurEau
import math

app = Flask(__name__)


def response_body(fullfillment_text, display_text):
    return {
        "fulfillmentText": fullfillment_text,
        "displayText": display_text,
        "source": "hackathon2020"
    }


def hour_intent():
    msg = "il est {} heure".format(str(datetime.now()))
    return response_body(msg, msg)

def pleine_mer_intent(ville):
    msg = "la mer sera pleine a {}".format(getMaree(ville,"11/10/2020","pm"))
    msg = msg + " et le coefficient sera de {}.".format(getCoef(ville,"11/10/2020"))
    return response_body(msg, msg)

def meteo_marine_intent(ville):
    msg = condition_climat.getMeteoMarine(ville)
    
    #     msg = "Bulletin côte 'La Hague – Penmarc'h' matin Prévisions pour la journée du samedi 10 octobre VENT : Nord-Ouest 4 à 5, fraichissant 5 à 6 en Manche l'après-midi. MER : agitée. HOULE : Ouest à Nord-Ouest 2 m sur pointe Bretagne. TEMPS : Ciel nuageux. VISIBILITE : Bonne."
    
    return response_body(msg, msg)

def etat_mer_intent():
    msg = "La mer va être agitée, avec un vent contre-courant, sans doute plus calme côté sud."
    return response_body(msg, msg)

def hauteur_eau_intent(latitude,longitude):
    
    waterHeightInterrogator = HauteurEau()
    date = datetime.utcnow()
    
    data = waterHeightInterrogator.calculerHauteurDeau(latitude, longitude, date)
    
    print(data)
        
    hauteur = data.get("hauteur", 3)
    hauteur *= 10
    hauteur = math.ceil(hauteur)
    hauteur = hauteur / 10.
    
    duree = data["duree"]
     
    amplitude = data["amplitude"]
    amplitude *= 10
    amplitude = math.ceil(amplitude)
    amplitude = amplitude / 10.
    
    msg = "actuellement à votre position il y a {} m au-dessus du zéro. Cela va monter encore durant {] heures, de {} m. Voulez-vous un conseil pour le mouillage ?".format(hauteur,duree,amplitude)
    
    print(msg)
    
    return response_body(msg, msg)

def declaration_dauphins_intent():
    msg = "très bien, je reporte cette observation aux organismes intéressés."
    return response_body(msg, msg)

def default_intent():
    msg = "Je n'ai pas compris la question."
    return response_body(msg, msg)

def localisation_intent():
    return {
        "systemIntent": {
            "intent": "actions.intent.PERMISSION",
            "data": {
                "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec"
            }
        }
    }

@app.route("/thales_hackathon_2020", methods=["GET", "POST"])
def entry_api():
    myreq = json.loads(request.data)
    if myreq["queryResult"]["intent"]["displayName"] == "heure":
        return hour_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Meteo marine":
        try:
            ville = myreq["queryResult"]["parameters"]["location"]["city"]
        except TypeError:
            ville = "Brest"
        return meteo_marine_intent(ville)
    elif myreq["queryResult"]["intent"]["displayName"] == "Pleine mer":
        try:
            ville = myreq["queryResult"]["parameters"]["location"]["city"]
        except TypeError:
            ville = "Brest"
        return pleine_mer_intent(ville)
    elif myreq["queryResult"]["intent"]["displayName"] == "Hauteur eau":
        latitude = 47.44
        longitude = 4.4
        
        return hauteur_eau_intent(latitude,longitude)
    elif myreq["queryResult"]["intent"]["displayName"] == "Etat mer":
        return etat_mer_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Declaration dauphins":
        return declaration_dauphins_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Localisation":
        return localisation_intent()
    
if __name__ == "__main__":
    app.run(port=8456)
