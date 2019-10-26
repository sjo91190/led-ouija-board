import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = (2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21)

GPIO.setup(PIN, GPIO.OUT)
GPIO.output(16, GPIO.LOW)


def gpio_cycle():
    for item in PIN:
        GPIO.output(PIN[item], GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(PIN[item], GPIO.LOW)
        time.sleep(0.05)
        item += 1


def gpio_flash():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(PIN, GPIO.LOW)

gpio_cycle()
