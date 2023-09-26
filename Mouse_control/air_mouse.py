import serial
import time
import pyautogui

Arduino =serial.Serial("/dev/ttyACM0",19200)

while 1:
  data  =  str(Arduino.readline().decode('ascii'))   #read the data
  #time.sleep(0.1)
  print("ARDUINO::: " + data)
  if ";" not in data:
    continue
  roll, pitch = data.split(";")
  print(roll)
  print(pitch)