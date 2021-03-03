# Project:		IoT Auto-Gardener
# Program:		sensorread.py
# Purpose:		Establish a serial connection with the Arduino, receive values from it, and process that information
# Author(s):	Jared Wagler, Sean McGuffey, Mife Atewogbola, Mouhammed Diagne

# Import packages needed for connection
import serial
import time
import dataProcess.py   # Local file containing data processing for sensor values 

# Connect to Arduino over serial
def serialConnect():
    # Connect
    ser = serial.Serial('COM4',9600)
    time.sleep(2)
    
    # Return serial connection "ser"
    return ser
    
# Collect data from Arduino, runs continuously
def dataCollect(con):
    # set up an array to hold the sensor data
    data = []
    
    # Infinite loop to continuously collect data from Arduino
    while True:
        rawRead = con.readline()            # Read raw data from connection
        unicodeRead = rawRead.decode()      # Decode data into Unicode
        newlineRead = unicodeRead.rstrip()  # Remove newline characters (\n and \r)
        sensorVal = float(newlineRead)      # Convert data string into floating-point number
        
        print(sensorVal)                    # Print processed data to the user
        data.append(sensorVal)              # Add processed data to array
        processValues(data)                 # Send to data processing function
        time.sleep(0.1)                     # Wait before receiving data
