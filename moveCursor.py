#This python program will move your mouse cursor, 1cm down per second from starting point

import pyautogui
import time
while True:
	for i in range(0,100):
		pyautogui.moveTo(1000,i*10)
		time.sleep(0)
  
  
