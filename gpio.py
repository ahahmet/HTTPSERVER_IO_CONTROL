import RPi.GPIO as GPIO

class BoardGPIO:
    def __init__(self, pin_count):
        self.pin_count = pin_count

    #gpio initialize
    def gpio_init(self, pins):
        GPIO.setmode(GPIO.BCM)
        for i in range(len(self.pin_count)):
            GPIO.setup(pins[i], GPIO.OUT)

    def output_on(self, index):
        GPIO.output(index, GPIO.HIGH)

    def output_off(self, index):
        GPIO.output(index, GPIO.LOW)

    def gpio_cleanUp(self):
        GPIO.cleanup()
