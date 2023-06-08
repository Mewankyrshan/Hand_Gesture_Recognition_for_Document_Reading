1. Collect accelerometer data in Data Collection folder
2. Train the model with collected data in Model Training folder
3. Copy the model.h file obtained from Model Training into the classifying_tflite folder
4. Upload the classifying_tflite sketch to the arduino board
5. Open the navigation python script and run it

The arduino will recognize performed gestures and the python script will map these gestures to corresponding navigaiton functions.