# -*- coding: utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)


@app.route("/thales_hackathon_2020", methods=["GET", "POST"])
def entry_api():
    myreq = json.loads(request.data)
    print(json.dumps(myreq, indent=4))
    myparameters = list(myreq["queryResult"]["parameters"].values())
    return {
        "fulfillmentText": "la somme est : " + str(int(sum(myparameters))),
        "displayText": "Hello jo",
        "source": "hackathon2020"
    }


if __name__ == "__main__":
    app.run()
