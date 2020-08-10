from time import sleep
from string import ascii_uppercase
# from gpiozero import LEDBoard, LED


PIN = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26,
       14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

ALPHA = [_ for _ in ascii_uppercase]

PINOUT = dict(zip(ALPHA, PIN))
# LED_ARRAY = LEDBoard(PIN)


def gpio_cycle():

    # for led in LED_ARRAY:
    #     led.on()
    #     sleep(0.05)
    #     led.off()
    #     sleep(0.05)
    for key, value in PINOUT.items():
        print(f"{key.upper()}: ON ({value})")
        sleep(0.5)
        print(f"{key.upper()}: OFF ({value})")
        sleep(0.05)


def gpio_flash(count):

    for times in range(count):
        print("ALL ON")
        # LED_ARRAY.on()
        sleep(0.07)
        # LED_ARRAY.off()
        print("ALL OFF")
        sleep(0.07)


def letter(n):

    led = PINOUT[n.upper()]

    # LED(led).on()
    print(f"LETTER: {n.upper()}: ON ({led})")
    sleep(0.5)
    # LED(led).off()
    print(f"LETTER: {n.upper()}: OFF ({led})")
    sleep(0.5)


def run_phrase(phrase: str):
    phrase = [_ for _ in phrase]
    print(phrase)

    for char in phrase:
        if char.upper() in ascii_uppercase:
            letter(char.upper())
        else:
            sleep(1)



