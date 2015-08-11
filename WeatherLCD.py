import time
import timeit
import os
import pywapi
import string 
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1.0, 0, 0)

message = "hi"
lcd.clear()
lcd.message(message)
time.sleep(0.1)

#loc_ID = pywapi.get_location_ids('mckees rock, pa')

#print(loc_ID)

#print "Yahoo says: It is " + string.lower(wDATA['condition']['text']) + " and " + wDATA['condition']['temp']

while True:

	wDATA = pywapi.get_weather_from_yahoo('USPA1014','imperial')	
	
	Wcond = string.lower(wDATA['condition']['text'])
	Wtemp = string.lower(wDATA['condition']['temp'])	
	
	#lcd.set_color(1.0, 0, 0)	

	flag = 1
	
	if  flag > 0:
		
		time.sleep(2.8)	
		#message = 
		lcd.clear()
		lcd.message(str(Wtemp) + "F" + "\n%s "%Wcond)
		time.sleep(10.0)
		#lcd.clear()
		#lcd.message("Temp is\n" + str(Wtemp) + chr(223) + "C")
		time.sleep(10.0*60)
		
		flag = 0
		del wDATA
		del Wcond
		del Wtemp
			
		 	
