import RPi.GPIO as GPIO

class BoardGPIO:
    def __init__(self, pin_count):
        self.pin_count = pin_count

    #gpio initialize
    def gpio_init(self):
        GPIO.setmode(GPIO.BCM)
        for i in range(len(self.pin_count)):
            GPIO.setup(i, GPIO.OUT)

    def output_on(index):
        GPIO.output(index, GPIO.HIGH)

    def output_off(index):
        GPIO.output(index, GPIO.LOW)
