from os import urandom, path
from waitress import serve
from multiprocessing import Process
from paste.translogger import TransLogger
from flask import Flask, request, render_template, redirect, url_for, session
from ouija_board.db import DBOperations
from ouija_board import config as led

rel_path = path.abspath(path.dirname(__file__))
db_path = path.join(rel_path, "phrase.db")

phrase_db = DBOperations(db_path)

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
    phrase_db.update(phrase)
    return render_template("response.html", phrase=phrase)


def start_server():
    host = "0.0.0.0"
    port = 5000
    # ouija.run(host=host, port=port, debug=True, use_reloader=False)
    serve(TransLogger(ouija), host=host, port=port)


def phrase_loop():

    # led.gpio_cycle()
    led.gpio_flash(2)

    while True:
        try:
            led.run_phrase(phrase_db.retrieve())
            print(phrase_db.retrieve())
        except KeyboardInterrupt:
            quit()


if __name__ == "__main__":
    Process(target=start_server, args=()).start()
    phrase_loop()

