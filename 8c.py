# Importeer de RPi.GPIO bibliotheek
import RPi.GPIO as GPIO

# ledpin nummers
LED_ONE = 2
LED_TWO = 3
ARDUINO_CONNECTOR = 17


GPIO.setmode(GPIO.BCM)

# Stel de LED-pinnen en de Arduino-connector pin in als uitgangen
GPIO.setup(LED_ONE, GPIO.OUT)
GPIO.setup(LED_TWO, GPIO.OUT)
GPIO.setup(ARDUINO_CONNECTOR, GPIO.OUT)


try:
    # Herhaal
    while True:
        # Controleer of de Arduino-connector op HIGH staat
        if GPIO.input(ARDUINO_CONNECTOR) == GPIO.HIGH:
            print("actief")
            GPIO.output(LED_ONE, GPIO.HIGH)  # Zet LED_ONE aan
            GPIO.output(LED_TWO, GPIO.LOW)   # Zet LED_TWO uit

        # Controleer of de Arduino-connector op LOW staat
        elif GPIO.input(ARDUINO_CONNECTOR) == GPIO.LOW:
            print("niet actief")
            GPIO.output(LED_ONE, GPIO.LOW)   # Zet LED_ONE uit
            GPIO.output(LED_TWO, GPIO.HIGH)  # Zet LED_TWO aan

# GPIO-pinnen opgeruimd
finally:
    GPIO.cleanup()
