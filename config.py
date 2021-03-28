from os import path, urandom
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
db_path = path.join(base_dir, "phrase.db")
env_path = path.join(base_dir, ".env")


def get_env() -> None:
    """This function reads in your .env file and sets the environment variables

    :return: None
    :rtype: None
    :raises FileNotFoundError: When the .env cannot be located or isn't present
    """

    if path.isfile(env_path):
        load_dotenv(dotenv_path=env_path)

        return None

    raise FileNotFoundError("Could not locate .env file")


class Config:

    SECRET_KEY = urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(db_path)

    @staticmethod
    def init_app(app):
        pass
