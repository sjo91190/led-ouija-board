import json
import datetime
from flask import request
from app.api import api
from config import phrase_db


@api.route("/response", methods=["POST"])
def api_response():
    """API for the web app used for testing

    :return: Returns the phrase and timestamp
    """

    now = str(datetime.datetime.now())
    remote_ip = request.remote_addr
    phrase = json.loads(request.data)

    phrase_db.insert(now, remote_ip, phrase["phrase"])
    resp = {"phrase": phrase["phrase"], "time": now}

    return json.dumps(resp), 201
