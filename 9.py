import RPi.GPIO as GPIO
import time

# pinnummers instellen arduino
ArduinoPin = [11, 9, 10, 22]

# LED pins instellen
LEDPins = [26, 19, 13, 6]

# Houd de tijd bij voor elke LED
lastTimes = [0, 0, 0, 0]

# Stel vertragingen in voor elke LED
delays = [500, 500, 0, 0]

# bijhouden van de geselecteerde LED
selectedLed = -1

# Stel de GPIO-modus in
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(ArduinoPin[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for i in range(4):
    GPIO.setup(LEDPins[i], GPIO.OUT)

# Functie om de tijd in milliseconden te retourneren
def millis():
    return time.time() * 1000

# Functie om de vertraging voor een LED in te stellen
def setDelay(index, delay):
    delays[index] = delay

# Functie om inputsignalen van Arduino te controleren
def checkForInput():
    global selectedLed
    for i in range(4):
        if GPIO.input(ArduinoPin[i]):
            time.sleep(0.05)
            newI = i + 1
            if selectedLed == -1:
                selectedLed = i
            else:
                setDelay(selectedLed, newI * 100)
                selectedLed = -1

# leds aansturen
def loop():
    global lastTimes
    for i in range(4):
        # Controleer of de ingestelde tijd
        if millis() - lastTimes[i] >= delays[i]:
            lastTimes[i] = millis()
            # Wissel de status van de LED
            GPIO.output(LEDPins[i], not GPIO.input(LEDPins[i]))

# functies aanroepen
while True:
    checkForInput()
    loop()
