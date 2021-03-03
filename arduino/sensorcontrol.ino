// Project:		IoT Auto-Gardener
// Program:		sensorcontrol.ino
// Purpose:		Establish a serial connection with the Raspberry Pi and send sensor values to it
// Author(s):	Jared Wagler, Sean McGuffey, Mife Atewogbola, Mouhammed Diagne

//Definitions
int humidPin = A0;
int tempPin = A1;
int moistPin = A2;

//Create array to hold sensor values
//Array location [0] is Humidity
//Array location [1] is Temperature
//Array location [2] is Moisture
int sensorValues [3];

//Establish Serial Connection
void setup() {
	//Determine pin layout of sensors
	pinMode(humidPin, INPUT);
	pinMode(tempPin, INPUT);
	pinMode(moistPin, INPUT);
	
	//Start serial connection
	Serial.begin(9600);
}

void loop() {
	//Obtain current values from both sensors
	sensorValues[0] = analogRead(humidPin,);
	sensorValues[1] = analogRead(tempPin);
	sensorValues[2] = analogRead(moistPin);
	
	//Do only if serial connection is online
	if (Serial.available() != 0) {
		//Sends sensor values to Raspberry Pi over serial
		Serial.println(sensorValues);
	}
	
	//Set a 100 ms delay between readings
	delay(100);
}
