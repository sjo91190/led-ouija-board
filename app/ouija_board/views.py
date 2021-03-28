from flask import request, render_template, redirect, url_for, session
import datetime
from app import db
from app.ouija_board import ouija
from app.models import OuijaPhrase


@ouija.route("/", methods=['GET', 'POST'])
def index():
    """Landing page for the web app

    :return: Returns the web page
    """

    session["phrase"] = request.form.get("phrase")

    if request.method == "GET":
        return render_template("index.html")

    return redirect(url_for("ouija.response"), 302)


@ouija.route("/response", methods=["GET"])
def response():
    """Response page for the web app

    :return: Returns your submitted phrase
    """

    now = str(datetime.datetime.now())
    remote_ip = request.remote_addr
    phrase = session["phrase"]

    insert_phrase = OuijaPhrase(timestamp=now, remote_ip=remote_ip, phrase=phrase)
    db.session.add(insert_phrase)
    db.session.commit()

    return render_template("response.html", phrase=phrase)
