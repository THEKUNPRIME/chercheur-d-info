from flask import Flask, redirect, url_for, render_template, request
#import requests
from requests.exceptions import MissingSchema
import webscrapping as web
import pdfsearching as pdf

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    try:
        if request.method == "POST":
            user = request.form.get("nm")
            f = request.files.get("file")
            if user and user.strip() != "":
                if pdf.is_valid_pdf(user):
                    contacts = pdf.info_looking_pdf(user)
                    return render_template("home.html", contacts=contacts)

                elif web.url_exists(user):
                    contacts = web.info_looking_url(user)
                    return render_template("home.html", contacts=contacts)

                else:
                    return render_template("home.html", contacts=["URL ou chemin PDF invalide"])
            elif f:
                contacts = pdf.info_looking_pdf(f)
                return render_template("home.html", contacts=contacts)
        return render_template("home.html")

    except MissingSchema:
        return render_template("home.html", contacts=["⚠️ URL invalide (mauvaise forme)"])
    except FileNotFoundError:
        return render_template("home.html", contacts=["⚠️ Fichier PDF introuvable"])
    except TypeError:
        return render_template("home.html", contacts=["⚠️ URL inexistante (bonne forme mais n’existe pas)"])

#p-UaLWrc2_zD/=c

if __name__ == "__main__":
    app.run(debug=True)

"""schoolap, ascitech, vodacom et airtel"""