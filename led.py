import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED1 = 5
LED2 = 6
SW1 = 9
SW2 = 11
led1status = False
led2status = False
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(SW1,GPIO.IN)
GPIO.setup(SW2,GPIO.IN)
class led_control(object):
	def led1on(self):
		GPIO.output(LED1,True)
	def led1off(self):
                GPIO.output(LED1,False)

	def led2on(self):
		GPIO.output(LED2,True)
	def led2off(self):
                GPIO.output(LED2,False)

	def readbutton1(self):
		return GPIO.input(SW1)
	
	def readbutton2(self):
                return GPIO.input(SW2)

	def readstatusled1(self):
		return GPIO.input(LED1)
	def readstatusled2(self):
                return GPIO.input(LED2)

