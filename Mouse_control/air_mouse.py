import serial
import pyautogui

ser = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

while True:
    try:
        # Read a line from the serial port
        data = ser.readline().decode().strip()
        
        roll, pitch = data.split(';')

        print("Roll: " + roll + "   Pitch: " + pitch)

        roll = float(roll)
        pitch = float(pitch)
        
        pyautogui.move(roll*3, pitch*(-2))
        
    
    except KeyboardInterrupt:
        print("Program terminated by user.")
        break
    
    except Exception as e:
        print(f"Error: {str(e)}")