import serial

# Open a serial connection to the Arduino Nano
ser = serial.Serial('COM4', 9600)

# Open the file for writing, change file name as necessary
with open('counter.txt', 'w') as f:

    # Write the header row
    f.write('aX,aY,aZ,gX,gY,gZ\n')

    # Read and write accelerometer data to the file
    while True:
        if ser.in_waiting > 0:
            # Read the accelerometer data from the serial connection
            data = ser.readline().decode('utf-8').strip().split(',')

            # Write the accelerometer data to the file
            f.write(','.join(data) + '\n')
            print(data)

# The serial connection and file are automatically closed when the 'with' block is exited
