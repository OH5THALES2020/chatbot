# -*- coding: utf-8 -*-

from flask import Flask, request
import json
from datetime import datetime

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

@app.route("/thales_hackathon_2020", methods=["GET", "POST"])
def entry_api():
    myreq = json.loads(request.data)
    if myreq["intent"]["displayName"] == "heure":
        return hour_intent()
    myparameters = list(myreq["queryResult"]["parameters"].values())
    return response_body(
            "la somme est : " + str(int(sum(myparameters))),
            "Hello jo"
        )


if __name__ == "__main__":
    app.run(port=8456)
