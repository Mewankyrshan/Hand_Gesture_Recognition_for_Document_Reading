# Import necessary libraries
import serial
import pyautogui
import keyboard
import mouse

# set the serial port and baud rate to match the Arduino
ser = serial.Serial('COM3', 9600)
subprocess.Popen('C:/Program Files (x86)/Adobe/Reader 10.0/Reader/AcroRd32.exe')

while True:
    # read a line of text from the serial port
    data = ser.readline().decode('utf-8').rstrip()

    # print the line
    print(data)
    gesture = str(data)
    if gesture == 'down':
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
    if str(data) == 'up':
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
    if gesture == 'circle':
        # zoom in and out
        # zoom in
        keyboard.press('ctrl')
        keyboard.press_and_release('+')
        keyboard.release('ctrl')
    if str(data) == 'counter':
        # zoom out
        keyboard.press('ctrl')
        keyboard.press_and_release('-')
        keyboard.release('ctrl')
    if str(data) == 'pan':
        # rotate the screen clockwise
        keyboard.press('ctrl')
        keyboard.press('shift')
        keyboard.press_and_release('+')
        keyboard.release('shift')
        keyboard.release('ctrl')


