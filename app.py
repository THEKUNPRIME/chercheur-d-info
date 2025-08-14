#from click import MissingParameter
from flask import Flask, redirect, url_for, render_template, request
#import requests
from requests.exceptions import MissingSchema

#from utils import is_valid_email
import webscrapping as web

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    try:
        if request.method == "POST":
            user = request.form["nm"]
            contacts = (web.info_looking(user))
            return render_template("home.html", contacts=contacts)
        else:
            return render_template("home.html")
    except  MissingSchema:
        contacts = ["ca n'a pas la forme d'un url"]
        return render_template("home.html", contacts=contacts)
    except TypeError:
        contacts = ["url inéxistante(ca a une forme mais ca n'existe pas)"]
        return render_template("home.html", contacts=contacts)
#p-UaLWrc2_zD/=c

if __name__ == "__main__":
    app.run(debug=True)
