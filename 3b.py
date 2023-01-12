#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#leds instellen
LED_PIN2 = 2
LED_PIN3 = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
#leds om en om laten knipperen
while True:
    #als led 2 1 seconde aan is zal led 3 1 seconde uit zijn
    #1seconde aan
    GPIO.output(LED_PIN2, GPIO.HIGH)
    time.sleep(1)
    #1seconde uit
    GPIO.output(LED_PIN2, GPIO.LOW)
    time.sleep(1)
    #1seconde aan
    GPIO.output(LED_PIN3, GPIO.HIGH)
    time.sleep(1)
    #1seconde uit
    GPIO.output(LED_PIN3, GPIO.LOW)
    time.sleep(1)
