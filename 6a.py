#import gpio library
import RPi.GPIO as GPIO
#import sleep functie
import time

#buttons en servomotor pin instellen
BUTTON_PIN19 = 19
BUTTON_PIN13 = 13
MOTOR5 = 5

#setup buttons en motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN19, GPIO.IN)
GPIO.setup(BUTTON_PIN13, GPIO.IN)
GPIO.setup(MOTOR5, GPIO.OUT)

#pwm
pwm = GPIO.PWM(MOTOR5, 50)
pwm.start(0)
hoek = 0

def SetAngle(angle):
    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)

while True:
    #Snelheid per knop
    slow = GPIO.input(BUTTON_PIN13)
    fast = GPIO.input(BUTTON_PIN19)
    if slow or fast:

        #heen
        while hoek < 120:
            SetAngle(hoek)
            time.sleep(0.1)
            if GPIO.input(BUTTON_PIN19):
                time.sleep(0.1)
            hoek = hoek + 30

        #terug
        while hoek > 0:
            SetAngle(hoek)
            time.sleep(0.1)
            if GPIO.input(BUTTON_PIN19):
                time.sleep(0.1)

            hoek = hoek - 30
