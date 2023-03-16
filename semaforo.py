from time import sleep

import RPi.GPIO as GPIO

global ON
ON = True

ledRosso = 3
ledGiallo = 4
ledVerde = 17
ledVerdePedone = 27
bottone = 2

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledRosso, GPIO.OUT)
GPIO.setup(ledGiallo, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(ledVerdePedone, GPIO.OUT)
GPIO.setup(bottone, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def pedone(channel):
    global ON
    ON = False
    GPIO.output(ledRosso, GPIO.LOW)
    GPIO.output(ledGiallo, GPIO.LOW)
    GPIO.output(ledVerde, GPIO.LOW)
    GPIO.output(ledVerdePedone, GPIO.LOW)

    GPIO.output(ledRosso, GPIO.HIGH)
    GPIO.output(ledVerdePedone, GPIO.HIGH)
    sleep(5)
    GPIO.output(ledVerdePedone, GPIO.LOW)
    GPIO.output(ledRosso, GPIO.LOW)
    ON = True


GPIO.add_event_detect(bottone, GPIO.FALLING, callback=pedone, bouncetime=1000)

if __name__ == '__main__':
    try:
        while True:
            if ON:
                GPIO.output(ledRosso, GPIO.HIGH)
                sleep(5)
            if ON:
                GPIO.output(ledRosso, GPIO.LOW)
            if ON:
                GPIO.output(ledGiallo, GPIO.HIGH)
                sleep(2)
                GPIO.output(ledGiallo, GPIO.LOW)
            if ON:
                GPIO.output(ledVerde, GPIO.HIGH)
                sleep(3)
                GPIO.output(ledVerde, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.output(ledRosso, GPIO.LOW)
        GPIO.output(ledGiallo, GPIO.LOW)
        GPIO.output(ledVerde, GPIO.LOW)
        GPIO.output(ledVerdePedone, GPIO.LOW)
        GPIO.cleanup()
