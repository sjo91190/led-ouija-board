from time import sleep
from gpiozero import LED
from os import urandom
from flask import Flask, request, json, render_template, redirect, url_for, session
from waitress import serve
from paste.translogger import TransLogger

pinout = {"a": 2, "b": 3, "c": 4, "d": 17, "e": 27, "f": 22, "g": 10, "h": 9, "i": 11, "j": 5,
          "k": 6, "l": 13, "m": 19, "n": 26, "o": 14, "p": 15, "q": 18, "r": 23, "s": 24, "t": 25,
          "u": 8, "v": 7, "w": 12, "x": 16, "y": 20, "z": 21}

ouija = Flask(__name__)
ouija.secret_key = urandom(24)


@ouija.route("/", methods=['GET', 'POST'])
def index():
    session["phrase"] = request.form.get("phrase")

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        return redirect(url_for("response"), 302)


@ouija.route("/response", methods=["GET"])
def response():
    phrase = session["phrase"]
    return render_template("response.html", phrase=phrase)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    ouija.run(host=host, port=port, debug=True)
    # serve(TransLogger(ouija), host=host, port=port)
