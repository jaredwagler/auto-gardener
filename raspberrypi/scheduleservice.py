# Project:        IoT Auto-Gardener
# Program:        scheduleservice.py
# Purpose:        Take values sent by the sensorread.py program and control the scheduling of the plant's light and water
# Author(s):      Jared Wagler, Sean McGuffey, Mife Atewogbola, Mouhammed Diagne

from datetime import datetime

# Mode control.
# 0 = Automatic schedule mode (Uses values defined below)
# 1 = As-Needed mode (Waters the plants when needed as determined by the sensors and weather data)
# 2 = User control (User controls functions through the web application)
OPERATION_MODE = 0

# user-controlled values
# formatted in HHMMSS format
# Ex: 4:34:06 PM would be listed as 163406

LIGHT_ON = 063000 # What time the light turns on each day
LIGHT_OFF = 190000 # What time the light turns off each day
LIGHT_STATE = 0 # Current state of the light, 0 is off, 1 is on

WATER_TIMES = [083000, 153000] # Array to allow for multiple waterings per day
WATER_DURATION = 10 # Time, in seconds, to water the plant at a time
WATER_THRESHOLD = 50 # Water moisture threshold, in percentage (0-100) to determine when to water the plant

# Take data from sensors
def processValues(sensorData):
    currentTime = int(datetime.now().replace(:, '')) # Formats the time correctly
    
    if (OPERATION_MODE == 1):
        # releases water if needed
        if (sensorData[2] <= WATER_THRESHOLD):
            releaseWater(WATER_DURATION) # Sends data to function to release water to the plants

        # turns on light as scheduled
        if ((LIGHT_STATE == 0) && (LIGHT_ON < currentTime < LIGHT_OFF):
            toggleLight()
            LIGHT_STATE = 1
        
        # turns off light as scheduled
        if ((LIGHT_STATE == 1) && ((currentTime < LIGHT_ON) || (currentTime > LIGHT_OFF)):
            toggleLight()
            LIGHT_STATE = 0
            
    elif (OPERATION_MODE == 2):
        # Code for interfacing to web client
    else:
        # Check if water should be released
        i = 0
        SCHEDULE_MATCH = 0
        while (i < len(WATER_TIMES)):
            if WATER_TIMES(i) == currentTime:
                SCHEDULE_MATCH = 1
            i += 1
        
        # turns on water as scheduled
        if (SCHEDULE_MATCH == 1):
            releaseWater(WATER_DURATION) # Sends data to function to release water to the plants

        # turns on light as scheduled
        if ((LIGHT_STATE == 0) && (LIGHT_ON < currentTime < LIGHT_OFF):
            toggleLight()
            LIGHT_STATE = 1
        
        # turns off light as scheduled
        if ((LIGHT_STATE == 1) && ((currentTime < LIGHT_ON) || (currentTime > LIGHT_OFF)):
            toggleLight()
            LIGHT_STATE = 0
