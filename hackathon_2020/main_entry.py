# -*- coding: utf-8 -*-

from flask import Flask, request
import json
from datetime import datetime
import condition_climat
from horairesMarees import *

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

def pleine_mer_intent():
    heure = getMaree("brest","10/10/2020","pm")
    heure_list = heure[0].split(':')
    result = heure_list[0] + 'h'+ heure_list[1] 
    msg = "la mer sera pleine a {}".format(result)
    msg = msg + " et le coefficient sera de 95."
    return response_body(msg, msg)

def meteo_marine_intent():
    msg = condition_climat.getMeteoMarine("Brest")
    
    #     msg = "Bulletin côte 'La Hague – Penmarc'h' matin Prévisions pour la journée du samedi 10 octobre VENT : Nord-Ouest 4 à 5, fraichissant 5 à 6 en Manche l'après-midi. MER : agitée. HOULE : Ouest à Nord-Ouest 2 m sur pointe Bretagne. TEMPS : Ciel nuageux. VISIBILITE : Bonne."
    
    return response_body(msg, msg)

def etat_mer_intent():
    msg = "La mer va être agitée, avec un vent contre-courant, sans doute plus calme côté sud."
    return response_body(msg, msg)

def hauteur_eau_intent():
    msg = "actuellement à votre position il y a 4 m au-dessus du zéro. Cela va monter encore durant 3 heures, de 3 m. Voulez-vous un conseil pour le mouillage ?"
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
        return meteo_marine_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Pleine mer":
        return pleine_mer_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Hauteur eau":
        return hauteur_eau_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Etat mer":
        return etat_mer_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Declaration dauphins":
        return declaration_dauphins_intent()
    elif myreq["queryResult"]["intent"]["displayName"] == "Localisation":
        return localisation_intent()
    
if __name__ == "__main__":
    app.run(port=8456)
