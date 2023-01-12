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
#leds laten knipperen
while True:
    #led 2 1.3 seconde aan
    GPIO.output(LED_PIN2, GPIO.HIGH)
    time.sleep(1.3)
    #led 2 0.7 seconde uit
    GPIO.output(LED_PIN2, GPIO.LOW)
    time.sleep(0.7)
    #led 3 0.8 seconde aan
    GPIO.output(LED_PIN3, GPIO.HIGH)
    time.sleep(0.8)
    #led 3 1.7 seconde uit
    GPIO.output(LED_PIN3, GPIO.LOW)
    time.sleep(1.7)
