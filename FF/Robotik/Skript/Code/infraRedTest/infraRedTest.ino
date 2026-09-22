#include <IRSensor.h>

IRSensor irSensor(0);    //Connect to Analog Pin 0 (yellow)

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  unsigned int irValue = irSensor.readSensorValue();
  Serial.print("IR= ");
  Serial.println(irValue);
  delay(1000);
}
