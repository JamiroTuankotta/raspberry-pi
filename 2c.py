import RPi.GPIO as GPIO
import time
#led instellen
LED_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#led laten knipperen
while True:
    #led 0.1 seconde aan zetten
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    #led 0.1 seconde uit zetten
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)

