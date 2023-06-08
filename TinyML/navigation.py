# Import necessary libraries
import serial

import subprocess
# Mouse library for mouse control
import mouse
# Keyboard library for keyboard control
import keyboard

# Open application
subprocess.Popen('C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe')
# Open a serial connection to the Arduino Nano
ser = serial.Serial('COM3', 9600)

while True:
    if ser.in_waiting > 0:
        # Read the accelerometer data from the serial connection
        data = ser.readline().decode().strip().split()
        gesture = str(data)
        print(gesture)
        if str(data) == '[\'down\']':
            # scroll down
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
            mouse.wheel(-1)
        if str(data) == '[\'up\']':
            # scroll up
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
            mouse.wheel(1)
        if str(data) == '[\'circle\']':
            # zoom in
            keyboard.press('ctrl')
            keyboard.press_and_release('+')
            keyboard.release('ctrl')
        if str(data) == '[\'counter\']':
            # zoom out
            keyboard.press('ctrl')
            keyboard.press_and_release('-')
            keyboard.release('ctrl')
        if str(data) == '[\'pan\']':
            # rotate the screen clockwise
            keyboard.press('ctrl')
            keyboard.press('shift')
            keyboard.press_and_release('+')
            keyboard.release('shift')
            keyboard.release('ctrl')

# The serial connection and file are automatically closed when the 'with' block is exited
