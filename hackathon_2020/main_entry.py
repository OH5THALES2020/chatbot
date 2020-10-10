# -*- coding: utf-8 -*-

from flask import Flask, request
import json

app = Flask(__name__)


def response_body(fullfillment_text, display_text):
    return {
        "fulfillmentText": fullfillment_text,
        "displayText": display_text,
        "source": "hackathon2020"
    }


@app.route("/thales_hackathon_2020", methods=["GET", "POST"])
def entry_api():
    myreq = json.loads(request.data)
    myparameters = list(myreq["queryResult"]["parameters"].values())
    return response_body(
            "la somme est : " + str(int(sum(myparameters))),
            "Hello jo"
        )


if __name__ == "__main__":
    app.run(port=8456)
