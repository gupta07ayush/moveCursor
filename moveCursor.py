#This python program will move your mouse cursor, 1cm down per second from starting point
#NOTE: to stop the program move your cursor to the top left corner of your screen.

import pyautogui
import time
while True:
	for i in range(0,100):
		pyautogui.moveTo(1000,i*10)
		time.sleep(1)
  
  