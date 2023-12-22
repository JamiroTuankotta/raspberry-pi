# Importeer de bibliotheken
import RPi.GPIO as GPIO  # Geeft toegang tot GPIO-pinnen
import time              # Voor timingfuncties 

# LED pin
LED_PIN = 2

# Stel de pinnummering in (BCM is een van de schema's)
GPIO.setmode(GPIO.BCM)

# Stel de LED-pin in als uitgang
GPIO.setup(LED_PIN, GPIO.OUT)

# Functie om de LED te laten knipperen
def ledBlink():
    GPIO.output(LED_PIN, GPIO.HIGH)  # Zet de LED aan
    time.sleep(1)                    # Wacht 1 seconde
    GPIO.output(LED_PIN, GPIO.LOW)   # Zet de LED uit
    time.sleep(1)                    # Wacht nogmaals 1 seconde


try:
    while True:        # Blijf voor altijd herhalen
        ledBlink()     # Roep de knipperfunctie aan
finally:
    GPIO.cleanup()    # Maak de GPIO-pinnen schoon bij afsluiten
