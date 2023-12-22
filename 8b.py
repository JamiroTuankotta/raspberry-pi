# Importeer de  bibliotheken
import RPi.GPIO as GPIO  # Biedt toegang tot GPIO-pinnen
import time              # Voor timingfuncties 

#  LED-pinnen
LED_PIN = [2, 3]

# de knippertijden voor elke LED in milliseconden
blinkTime = [1000, 3000]

# Beginstatus van elke LED (uit)
ledStatus = [GPIO.LOW, GPIO.LOW]


GPIO.setmode(GPIO.BCM)

# Stel beide LED-pinnen in als uitgangen
GPIO.setup(LED_PIN[0], GPIO.OUT)
GPIO.setup(LED_PIN[1], GPIO.OUT)

# Functie om de huidige tijd in milliseconden te retourneren
def millis():
    return time.time() * 1000

# Bewaar de laatste knippertijd van elke LED
lastBlinkTime = [millis(), millis()]


try:
    while True:
        currentTime = millis()  # Huidige tijd in milliseconden

        # Update de status van beide LEDs
        GPIO.output(LED_PIN[0], ledStatus[0])
        GPIO.output(LED_PIN[1], ledStatus[1])

        # Controleer of LED 1 moet knipperen
        if currentTime - lastBlinkTime[0] >= blinkTime[0]:
            lastBlinkTime[0] = currentTime
            # Wissel de status van LED 1
            ledStatus[0] = GPIO.HIGH if ledStatus[0] == GPIO.LOW else GPIO.LOW

        # Controleer of LED 2 moet knipperen
        if currentTime - lastBlinkTime[1] >= blinkTime[1]:
            lastBlinkTime[1] = currentTime
            # Wissel de status van LED 2
            ledStatus[1] = GPIO.HIGH if ledStatus[1] == GPIO.LOW else GPIO.LOW

#  GPIO-pinnen worden opgeruimd
finally:
    GPIO.cleanup()
