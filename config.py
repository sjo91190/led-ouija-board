from os import path, urandom

base_dir = path.abspath(path.dirname(__file__))
db_path = path.join(base_dir, "phrase.db")


class Config:

    SECRET_KEY = urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(db_path)

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
