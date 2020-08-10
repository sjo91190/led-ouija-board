from time import sleep
from gpiozero import LED, LEDBoard

PIN = LEDBoard(2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21)


def gpio_cycle():
    for led in PIN:
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)


def gpio_flash(count):
    for times in range(count):
        PIN.on()
        sleep(0.07)
        PIN.off()
        sleep(0.07)


gpio_cycle()
gpio_flash(2)
