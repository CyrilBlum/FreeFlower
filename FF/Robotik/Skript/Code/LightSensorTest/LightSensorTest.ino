#include <LightSensor.h>

LightSensor lightSensor(1, 2);  //Analog Pin 1,2 green 
                              // and violet, braun to VCC
                              // 1: Rechts 2: links

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print("Light1= ");
  Serial.println(lightSensor.readSensorValue1());
  Serial.print("Light2= ");
  Serial.println(lightSensor.readSensorValue2());
  delay(400);
}
