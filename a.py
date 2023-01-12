#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#leds instellen
LED_PIN = 2, 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#beide leds laten knipperen
while True:
    #1 seconde aan
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    #1 seconde uit
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)