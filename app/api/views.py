import json
import datetime
from flask import request
from app.api import api
from app.models import OuijaPhrase
from app import db


@api.route("/set", methods=["POST"])
def api_response():
    """API for the web app used for testing

    :return: Returns the phrase and timestamp
    """

    now = str(datetime.datetime.now())
    remote_ip = request.remote_addr
    phrase = json.loads(request.data)

    insert_phrase = OuijaPhrase(timestamp=now, remote_ip=remote_ip, phrase=phrase['phrase'])
    db.session.add(insert_phrase)
    db.session.commit()

    resp = {"phrase": phrase["phrase"], "time": now}

    return json.dumps(resp), 201
