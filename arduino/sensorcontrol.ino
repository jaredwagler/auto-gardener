// Project:		IoT Auto-Gardener
// Program:		sensorcontrol.ino
// Purpose:		Establish a serial connection with the Raspberry Pi and send sensor values to it
// Author(s):		Jared Wagler, Sean McGuffey, Mife Atewogbola, Mouhammed Diagne

#include "DHT.h"
#define DHTPIN 3
#define DHTTYPE DHT22

//Definitions
int humidPin = A0;
int tempPin = A1;

//Establish Serial Connection
void setup() {
	//Create array to hold sensor values
	//Array location [0] is Humidity
	//Array location [1] is Temperature
	//Array location [2] is Moisture
	int sensorValues [3];
	
	//Determine pin layout of sensors
	pinMode(moistPin, INPUT);
	
	//Start serial connection
	Serial.begin(9600);
	
	dht.begin();
}

void loop() {
	//Obtain current values from both sensors
	sensorValues[0] = dht.readHumidity();
	sensorValues[1] = dht.readTemperature();
	sensorValues[2] = analogRead(moistPin);
	
	//Do only if serial connection is online
	if (Serial.available() != 0) {
		//Sends sensor values to Raspberry Pi over serial
		Serial.println(sensorValues);
	}
	
	//Set a 100 ms delay between readings
	delay(100);
}
