#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#led en button instellen
LED_PIN = 5
BUTTON_PIN = 6
#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
#button indrukken om led 1 sec te laten knipperen
while True:
    buttonState = GPIO.input(BUTTON_PIN)
#bij het indrukken van de button zal de led gaan knipperen
    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
        #1 seconde aan
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        #1seconde uit
        time.sleep(1)
        #bij het loslaten zal de led uit staan
    else:
        GPIO.output(LED_PIN, GPIO.LOW)