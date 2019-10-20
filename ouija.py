import time
import string
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = [2,3,4,17,27,22,10,9,11,5,6,13,19,26,14,15,18,23,24,25,8,7,12,16,20,21]
LET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z"]

def letter (n):
        for pin, let in zip(PIN,LET):
                if n == let:
                        GPIO.output(pin,GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(pin,GPIO.LOW)
                        time.sleep(0.5)

def run():
        with open("/home/pi/phrase.txt", "r") as ouijaSpeak:
                data = ouijaSpeak.read()
                for line in data:
                        if " " in line:
                                time.sleep(1)
                        if any(item in line for item in LET):
                                letter(line)

while True:
        try:
                GPIO.setup(PIN,GPIO.OUT)
                run()
                time.sleep(1)
        except KeyboardInterrupt:
                GPIO.output(PIN,GPIO.LOW)
                quit()
