import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
# Write Temperature Data to file
f = open("data.txt", "wb")

def callback(channel):
	if GPIO.input(channel):
		print ("Plants Watered!")
	else:
		print ("Plants Watered!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)


#ani = animation.FuncAnimation(fig, animate, interval=1000)

while True:
	temperature = sensor.get_temperature()
	print("The temperature is %s celsius" % temperature)
	f.write("%s\n" % temperature)
	GPIO.add_event_callback(channel,callback)
	time.sleep(1)
