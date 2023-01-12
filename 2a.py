#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#led 2 instellen
LED_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#led laten knipperen
while True:
    #led 1 seconde aan doen
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    #led 1 seconde uit zetten
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
