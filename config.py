from os import path
from app.db import DBOperations

base_dir = path.abspath(path.dirname(__file__))
db_path = path.join(base_dir, "phrase.db")

phrase_db = DBOperations(db_path)


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_RUN_HOST = "127.0.0.1"
    FLASK_RUN_PORT = 9000

    HOST = FLASK_RUN_HOST
    PORT = FLASK_RUN_PORT
    Debug = True


config = {
    "develop": DevelopmentConfig
}
