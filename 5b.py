#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time
#leds en buttons instellen
LED_PIN26 = 26
LED_PIN21 = 21
BUTTON_PIN6 = 6
BUTTON_PIN13 = 13

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN26, GPIO.OUT)
GPIO.setup(LED_PIN21, GPIO.OUT)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN13, GPIO.IN, GPIO.PUD_DOWN)
#gebruik millis
def millis():
    return time.time() * 1000

lastblinktime = millis()

try:
    while True:
        currenttime = millis()
        buttonState = GPIO.input(BUTTON_PIN13)
#als de button is ingedrukt zal led 21 0.7 seconde gaan knipperen
        if buttonState == GPIO.HIGH:
# 0.7 seconden
            if currenttime - lastblinktime >= 700:
                lastblinktime = currenttime

                GPIO.output(LED_PIN21, GPIO.HIGH) if GPIO.input(LED_PIN21) == GPIO.LOW else GPIO.output(LED_PIN21, GPIO.LOW)

#led 26 gaat uit
        else:
            GPIO.output(LED_PIN26, GPIO.LOW)


finally:
    GPIO.cleanup()