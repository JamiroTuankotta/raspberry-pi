import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # Vervang met de juiste seriele poort

try:
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Ontvangen van Arduino: {data}")
except KeyboardInterrupt:
    print("Programma gestopt")
    ser.close()
