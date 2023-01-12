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

while True:
    buttonState = GPIO.input(BUTTON_PIN)
    # bij het indrukken van de button zal led 5 1.3 seconde aan gaan
    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN5, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN5, GPIO.LOW)
        #led 5 7 seconde uit
        time.sleep(0.7)
        #led 19 zal uit staan
        GPIO.output(LED_PIN19, GPIO.LOW)
        #als de knop niet is ingedruik zal led 19 aan gaan
    else:
        GPIO.output(LED_PIN19, GPIO.HIGH)