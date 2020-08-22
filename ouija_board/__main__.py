"""This module exist so that the web app can be started via python -m"""

from time import sleep
from multiprocessing import Process
from .ouija import start_server, phrase_loop

Process(target=start_server, args=()).start()
sleep(1)
phrase_loop()
