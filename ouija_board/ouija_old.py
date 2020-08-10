import time
import RPi.GPIO as GPIO


time.sleep(4)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_let = {"a": 2, "b": 3, "c": 4, "d": 17, "e": 27, "f": 22, "g": 10, "h": 9, "i": 11, "j": 5, "k": 6, "l": 13,
           "m": 19, "n": 26, "o": 14, "p": 15, "q": 18, "r": 23, "s": 24, "t": 25, "u": 8, "v": 7, "w": 12, "x": 16,
           "y": 20, "z": 21}


def letter(n):
    GPIO.output(pin_let[n.strip('\n')], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin_let[n.strip('\n')], GPIO.LOW)
    time.sleep(0.5)


def run():
    with open("/home/pi/led-ouija-board/WebGUI/webphrase.txt", "r") as formatFile:
        wordform = "\n".join(formatFile).lower()
        for line in wordform:
            if " " in line:
                time.sleep(1)
            else:
                try:
                    letter(line)
                except KeyError:
                    time.sleep(1)


while True:
    try:
        GPIO.setup(list(pin_let.values()), GPIO.OUT)
        run()
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.output(list(pin_let.values()), GPIO.LOW)
        quit()
