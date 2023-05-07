import serial
import pyautogui
import subprocess

# set the serial port and baud rate to match the Arduino
ser = serial.Serial('COM3', 9600)
counter = 0
subprocess.Popen('C:/Program Files (x86)/Adobe/Reader 10.0/Reader/AcroRd32.exe')

while True:
    # read a line of text from the serial port
    data = ser.readline().decode('utf-8').rstrip()

    # print the line
    print(data)
    gesture = str(data)
    if gesture == 'up':
        # scroll up
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)
        pyautogui.scroll(100)

    if gesture == 'down':
        # scroll down
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)

    if gesture == 'circle':
        # zoom in and out
        if counter == 0:
            pyautogui.hotkey('ctrl', '2')
            counter = 1
        elif counter == 1:
            pyautogui.hotkey('ctrl', '1')
            counter = 0

    if gesture == 'pan':
        # rotate the screen clockwise
        pyautogui.hotkey('shift', 'ctrl', '+')



