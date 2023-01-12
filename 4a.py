#import gpio library
import RPi.GPIO as GPIO
#led en button instellen
LED_PIN = 5
BUTTON_PIN = 6
#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
#button indrukken om led te laten branden
while True:
    buttonState = GPIO.input(BUTTON_PIN)
#als de button is ingedrukt, zal de led aan zijn
    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
#anders zal de led uit zijn
    else:
        GPIO.output(LED_PIN, GPIO.LOW)