"""This module contains the flask web application"""
import sys
import datetime
from os import urandom, path
from waitress import serve
from paste.translogger import TransLogger
from flask import Flask, request, render_template, redirect, url_for, session, json
from ouija_board.db import DBOperations
from ouija_board import led

rel_path = path.abspath(path.dirname(__file__))
db_path = path.join(rel_path, "phrase.db")

phrase_db = DBOperations(db_path)
phrase_db.create()

ouija = Flask(__name__)
ouija.secret_key = urandom(24)


@ouija.route("/", methods=['GET', 'POST'])
def index():
    """Landing page for the web app

    :return: Returns the web page
    """

    session["phrase"] = request.form.get("phrase")

    if request.method == "GET":
        return render_template("index.html")

    return redirect(url_for("response"), 302)


@ouija.route("/response", methods=["GET"])
def response():
    """Response page for the web app

    :return: Returns your submitted phrase
    """

    now = datetime.datetime.now()
    remote_ip = request.remote_addr
    phrase = session["phrase"]
    phrase_db.insert(now, remote_ip, phrase)

    return render_template("response.html", phrase=phrase)


@ouija.route("/api/response", methods=["POST"])
def api_response():
    """API for the web app used for testing

    :return: Returns the phrase and timestamp
    """

    now = datetime.datetime.now()
    remote_ip = request.remote_addr
    phrase = json.loads(request.data)

    phrase_db.insert(now, remote_ip, phrase["phrase"])
    resp = {"phrase": phrase["phrase"], "time": now}

    return json.dumps(resp), 201


def start_server():
    """Function to start the web app"""
    host = "0.0.0.0"
    port = 5000
    serve(TransLogger(ouija), host=host, port=port)


def phrase_loop():
    """This function will grab the latest phrase from the database
    and run a function to display it"""

    led.gpio_cycle()
    led.gpio_flash(2)

    while True:
        try:
            led.run_phrase(phrase_db.retrieve())
        except KeyboardInterrupt:
            sys.exit()
