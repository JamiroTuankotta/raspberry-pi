# Importeer de RPi.GPIO bibliotheek
import RPi.GPIO as GPIO
# pinnummers instellen
BUTTON1 = 2
ARDUINOCONNECTOR = 17

GPIO.setmode(GPIO.BCM)
# Stel de knop in met een pull-down weerstand
GPIO.setup(BUTTON1, GPIO.IN, GPIO.PUD_DOWN)
# Arduino-connector in als uitgang
GPIO.setup(ARDUINOCONNECTOR, GPIO.OUT)
try:
    # Herhaal 
    while True:
        # Lees de status van de knop
        if GPIO.input(BUTTON1):
            # Wissel de status van de Arduino-connector
            GPIO.output(ARDUINOCONNECTOR, not GPIO.input(ARDUINOCONNECTOR))



# opgeruimd
finally:
    GPIO.cleanup()
