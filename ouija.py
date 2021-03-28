import sys
from multiprocessing import Process
from waitress import serve
from sqlalchemy import desc
from paste.translogger import TransLogger
from app import app_factory, led
from app.models import OuijaPhrase
from app import db

ouija_app = app_factory("develop")


def start_server():
    """Function to start the web app"""
    host = "127.0.0.1"
    port = 9000

    serve(TransLogger(ouija_app), host=host, port=port)


def phrase_loop():
    """This function will grab the latest phrase from the database
    and run a function to display it"""

    led.gpio_cycle()
    led.gpio_flash(2)

    while True:
        try:
            with ouija_app.app_context():
                phrase = db.session.query(OuijaPhrase.phrase).order_by(desc(OuijaPhrase.id)).first()
                if phrase:
                    led.run_phrase(phrase=phrase[0])
                else:
                    led.run_phrase(phrase="INIT")
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    Process(target=start_server, args=()).start()
    phrase_loop()
