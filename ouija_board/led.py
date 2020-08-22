"""This module contains functions to interface with the GPIO pins
on the raspberry pi"""
from time import sleep
from string import ascii_uppercase
from gpiozero import LEDBoard


PIN = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26,
       14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

ALPHA = list(ascii_uppercase)
NUM = list(range(26))

LED_ARRAY = LEDBoard(*PIN)

PINOUT = dict(zip(ALPHA, NUM))

LED_ARRAY[0].off()
LED_ARRAY[1].off()


def gpio_cycle():
    """This function cycles all LEDs, A-Z"""

    for led in LED_ARRAY:
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)

    # for led in PINOUT:
    #     print(f"{PINOUT[led]}: ON")
    #     sleep(0.05)
    #     print(f"{PINOUT[led]}: OFF")
    #     sleep(0.05)


def gpio_flash(count):
    """This function blinks all LEDs A-Z simultaneously"

    :param count: Count of how many times to blink
    """

    for _ in range(count):
        LED_ARRAY.on()
        sleep(0.07)
        LED_ARRAY.off()
        sleep(0.07)

    # for _ in range(count):
    #     print("ALL ON")
    #     sleep(0.07)
    #     print("ALL OFF")
    #     sleep(0.07)


def letter(char):
    """This function sets the pin corresponding to letter n to high

    :param char: The letter to illuminate
    """
    led = PINOUT[char.upper()]

    LED_ARRAY[led].on()
    sleep(0.5)
    LED_ARRAY[led].off()
    sleep(0.5)

    # print(f"{char.upper()} ({led}): ON")
    # sleep(0.5)
    # print(f"{char.upper()} ({led}): OFF")
    # sleep(0.5)


def run_phrase(phrase: str):
    """This function takes a phrase and displays it on the ouija board

    :param phrase: The phrase to display on the ouija board
    """
    phrase = list(phrase)
    sleep(1)
    for char in phrase:
        if char.upper() in ascii_uppercase:
            letter(char.upper())
        else:
            sleep(1)
