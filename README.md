# Roll no: B19CS017 CSE 8th Sem 
# Final Year Project 

## Topic: Hand Gesture Recognition for Document Reading
The project requires us to use hand gestures to document navigation. This can be achieved by using an accelerometer sensor such as the Arduno Nano 33 BLE which houses an in-built accelerometer.
This project uses the edge impulse website to train a model to use in the Arduino Nano 33 BLE. Accelerometer data is collected via Ardunio sensor and trained on a neural network model. The trained model is downloaded as a zip file.

Requirements:
Hardware:
Arduino Nano 33 BLE + USB Cable
Latptop

Software:
Arduino IDE
Python IDE - Pyserial & PyAutoGUI
PDF Reader (Adoce Acrobat Reader)

Steps:
1. Open the Arduino IDE and include the ei-gestures-arduino-1.0.5.zip library. DONE
1. Upload the project.ino sketch to the Arduino Nano 33 BLE. DONE
2. Open the pdf_gesture_control.py file and run it. (make changes as necessary)

The py file opens the Adobe Reader application and the 4 gestures (up, down, circle and pan) perform different gestures: scroll up, down, zoom in and out and rotate clockwise.
