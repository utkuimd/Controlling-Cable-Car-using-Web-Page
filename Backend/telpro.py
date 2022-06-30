import os
import time
import datetime
from time import sleep
import threading
import urllib2, urllib
import json

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


led_red = 13
led_green = 19
led_blue =26


coil_1_A_1_pin = 4
coil_1_A_2_pin = 17
coil_1_B_1_pin = 23
coil_1_B_2_pin = 24

buton_weight = 6

GPIO.setup(buton_weight, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

server_link = "http://192.168.1.24/"
link_get_command = server_link + "get_db_data.php"
link_set_rasp_status = server_link + "set_db_rasp_status.php"

weight_status = 'off'



class teleferik:
	cur_step = 1
	cur_pos = 0
	speed = 10
	
	direction = "wayB"
	start_stop = 1 # if 1 continue going if 0 -->stop
	
	steps_one_way = 260 # this number of steps must be taken in order to reach next point
	dest_pos = 0
	
	#coils
	ca1 = 0
	ca2 = 0
	cb1 = 0
	cb2 = 0

	

	def __init__(self, a1, a2, b1, b2):
		self.ca1 = a1
		self.ca2 = a2
		self.cb1 = b1
		self.cb2 = b2
		GPIO.setup(self.ca1, GPIO.OUT)
		GPIO.setup(self.ca2, GPIO.OUT)
		GPIO.setup(self.cb1, GPIO.OUT)
		GPIO.setup(self.cb2, GPIO.OUT)

	def disp_cur_pos(self):
		pos_per = int( self.cur_pos * 100 / self.steps_one_way) #position must be in range of 0-100.
		print ("Current position is %d" %spos_per)
		
	def get_cur_pos(self):
		pos_per = int( self.cur_pos * 100 / self.steps_one_way) #position must be in range of 0-100.
		return pos_per
	
	
	def get_cur_speed(self):
		return self.speed
		
	def get_direction(self):
		return self.direction;

	def get_stop_cnt(self):
		if self.start_stop == 1:
			return "Continue"
		elif self.start_stop == 0:
			return "Stop"
	

	def setStep(self, w1, w2, w3, w4):
		GPIO.output(self.ca1, w1)
		GPIO.output(self.ca2, w2)
		GPIO.output(self.cb1, w3)
		GPIO.output(self.cb2, w4)
	
	def forward(self, delay, steps):  
		for i in range(0, steps):
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)
				

	def backwards(self, delay, steps):  
		for i in range(0, steps):
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)
			
	
	def go(self, speed, steps):
		
		delay_t = speed;
		
		if steps < 0 :
			steps *= -1
			self.backwards(delay_t, steps)
			self.cur_pos -= 1
		elif steps > 0 :
			self.forward(delay_t, steps )
			self.cur_pos += 1
		
			
	def travel(self):
	
		if self.start_stop == 1: #proceed if there is no STOP command
			
			step = 0
			if self.direction == "forward":
				step = 1
			elif self.direction == "backward":
				step = -1 #one step backwards

				
			self.go(self.speed, step)
			
		else:
			time.sleep(0.1)
			
			
	
	def free(self):
		self.setStep(0,0,0,0)
 



# thread for teleferik A
def Tel_A():
	while 1:
		tela.travel()



#tela = teleferik(coil_1_A_1_pin, coil_1_A_2_pin, coil_1_B_1_pin, coil_1_B_2_pin)
tela = teleferik(  coil_1_B_2_pin , coil_1_B_1_pin, coil_1_A_2_pin, coil_1_A_1_pin)

#initialize thread for teleferik A
tel_a = threading.Thread(target=Tel_A)
tel_a.daemon = True
tel_a.start()


tela.stop_cnt = 1
tela.direction = "forward"
tela.speed = 0.004
tela.dest_pos = 999999

tela.go(0.005, 2)
tela.go(0.005, -2)

while True:
	contents = urllib2.urlopen(link_get_command).read()
	#print( contents )
	resp = json.loads(contents)
	
	
	time.sleep(.200)
	
	if resp['led_red'].find("on") >= 0:
		GPIO.output(led_red, 0)
	else:
		GPIO.output(led_red, 1)
        
	if resp['led_green'].find("on") >= 0:
		GPIO.output(led_green, 0)
	else:
		GPIO.output(led_green, 1)
		
	if resp['led_blue'].find("on") >= 0:
		GPIO.output(led_blue, 0)
	else:
		GPIO.output(led_blue, 1)

	#enable/disable motor
	if resp['motor_start_stop'].find("enable") >= 0:
		tela.start_stop = 1
	else:
		tela.start_stop = 0
	
	#set motor speed
	motor_speed = float(resp['motor_speed'])
	tela.speed = 0.022 -  motor_speed/5000.0

	#set motor direction
	if resp['motor_direction'].find("forward") >= 0:
		tela.direction = 'forward'
	else:
		tela.direction = 'backward'

		
	#Read button state	
	if GPIO.input(buton_weight) == True:
		weight_status = 'on'
	else:
		weight_status = 'off'
	
	
	
	#send raspberry status
	#http://192.168.1.17/set_db_rasp_status.php?weight=on&motor_cur_pos=-343&motor_is_en_dis=enabled
	
	link_set_rasp_status_temp = link_set_rasp_status
	
	#set weight status
	link_set_rasp_status_temp = link_set_rasp_status_temp + '?weight=' + weight_status
	
	#set motor current position
	link_set_rasp_status_temp = link_set_rasp_status_temp + '&motor_cur_pos=' + str(tela.cur_pos)
	
	#set motor enable/disable status
	if tela.start_stop == 1:
		link_set_rasp_status_temp = link_set_rasp_status_temp + '&motor_is_en_dis=enabled'
	else:
		link_set_rasp_status_temp = link_set_rasp_status_temp + '&motor_is_en_dis=disabled'
	
	#set motor speed status
	motor_speed_temp = int((0.022 - tela.speed)*5000)
	link_set_rasp_status_temp = link_set_rasp_status_temp + '&motor_speed=' + str(motor_speed_temp)

	
	#print( link_set_rasp_status_temp )
	
	#send GET query to server
	contents = urllib2.urlopen(link_set_rasp_status_temp).read()
		
	
