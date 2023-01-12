#rpi library
from RPi import GPIO
#import sleep functie
import time

#buttons en motor instellen
gpioPins = [6, 13, 19, 26]
BUTTON_PIN3 = 3
BUTTON_PIN4 = 4

#button en motor setup
GPIO.setmode(GPIO.BCM)
for p in gpioPins:
    GPIO.setup(p, GPIO.OUT)
GPIO.setup(BUTTON_PIN3, GPIO.IN)
GPIO.setup(BUTTON_PIN4, GPIO.IN)

#Snelheid bepalen van het indrukken van de knop
langzaam = (5 - 0.0) / (512 * 8)
snel = (12 - 0.0) / (512 * 8)

timer = 0

try:
    while True:
        ##knop1
        ##links en langzaam
        while GPIO.input(BUTTON_PIN3):
            for p in range(0, 4):
                for b in gpioPins:
                    GPIO.output(b, GPIO.LOW)
                GPIO.output(gpioPins[p], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + langzaam > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(p + 1) % 4], GPIO.HIGH)
                timer = time.perf_counter() 
                while timer + langzaam > time.perf_counter():
                    pass

                ##knop 2
                #rechts en snel
        while GPIO.input(BUTTON_PIN4):
            for p in range(3, -1, -1):
                for b in gpioPins:
                    GPIO.output(b, GPIO.LOW)
                GPIO.output(gpioPins[p], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + snel > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(p - 1) % 4], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + snel > time.perf_counter():
                    pass
        for b in gpioPins:
            GPIO.output(b, GPIO.LOW)
finally:
    GPIO.cleanup()