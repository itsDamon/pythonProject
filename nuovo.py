from time import sleep

import RPi.GPIO as GPIO

ledRosso = 3
ledGiallo = 4
ledVerde = 17
ledVerdePedone = 27
bottone = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledRosso, GPIO.OUT)
GPIO.setup(ledGiallo, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(ledVerdePedone, GPIO.OUT)
GPIO.setup(bottone, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(ledRosso, GPIO.LOW)
GPIO.output(ledGiallo, GPIO.LOW)
GPIO.output(ledVerde, GPIO.LOW)
GPIO.output(ledVerdePedone, GPIO.LOW)