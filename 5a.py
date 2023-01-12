#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#leds en button instellen
LED_PIN5 = 5
LED_PIN19 = 19
BUTTON_PIN = 6

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN5, GPIO.OUT)
GPIO.setup(LED_PIN19, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
#gebruik millies
def millis():
    return time.time() * 1000

lastblinktime = millis()

try:
    while True:
        currenttime = millis()
        buttonState = GPIO.input(BUTTON_PIN)
#button indrukken
        if buttonState == GPIO.HIGH:
#De led zal met gebruik van millis 1 seconde aan en uit gaan
#1 seconde
            if currenttime - lastblinktime >= 1000:
                lastblinktime = currenttime

                GPIO.output(LED_PIN5, GPIO.HIGH) if GPIO.input(LED_PIN5) == GPIO.LOW else GPIO.output(LED_PIN5, GPIO.LOW)

#led uit button niet ingedrukt
        else:
            GPIO.output(LED_PIN5, GPIO.LOW)


finally:
    GPIO.cleanup()