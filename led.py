import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED1 = 5
LED2 = 6
led1status = False
led2status = False
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
class led_control(object):
	def changeled1(self):
		global led1status
		led1status = not led1status
		GPIO.output(LED1,led1status)
		return led1status
	
	def changeled2(self):
		global led2status
		led2status = not led2status
		GPIO.output(LED2,led2status)
		return led2status
