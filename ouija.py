import sys
from multiprocessing import Process
from waitress import serve
from paste.translogger import TransLogger
from app import app_factory
from app.ouija_board import led
from config import phrase_db


def start_server():
    """Function to start the web app"""
    host = "127.0.0.1"
    port = 9000
    ouija_app = app_factory("develop")
    serve(TransLogger(ouija_app), host=host, port=port)


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


if __name__ == "__main__":
    phrase_db.create()
    Process(target=start_server, args=()).start()
    phrase_loop()
