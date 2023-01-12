#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time

#leds en button instellen
LED_PIN26 = 26
LED_PIN21 = 21
BUTTON_PIN19 = 19

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN19, GPIO.IN)
GPIO.setup(LED_PIN26, GPIO.OUT)
GPIO.setup(LED_PIN21, GPIO.OUT)

#gebruik millis
millis = time.time()

try:
    while True:
        if GPIO.input(BUTTON_PIN19):
#led 26 aan en led 21 uit
            GPIO.output(LED_PIN26, GPIO.HIGH)
            GPIO.output(LED_PIN21, GPIO.LOW)

            if millis +1 < time.time():
                GPIO.output(LED_PIN26, GPIO.LOW)
                GPIO.output(LED_PIN21, GPIO.HIGH)

            if millis +2 < time.time():
                millis = time.time()
        else:
            GPIO.output(LED_PIN26, GPIO.HIGH)
            GPIO.output(LED_PIN21, GPIO.LOW)
            if millis + 1.3 < time.time():
                GPIO.output(LED_PIN26, GPIO.LOW)
                GPIO.output(LED_PIN21, GPIO.HIGH)
            if millis + 2 < time.time():
                millis = time.time()

        time.sleep(0.1)
finally:
          GPIO.cleanup()








