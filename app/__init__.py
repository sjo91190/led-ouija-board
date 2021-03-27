from os import urandom
from flask import Flask
from config import config


def app_factory(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key = urandom(24)

    from app.ouija_board import ouija as ouija_blueprint
    app.register_blueprint(ouija_blueprint, url_prefix="/")

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
