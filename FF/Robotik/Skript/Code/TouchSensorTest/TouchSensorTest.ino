#include <TouchSensor.h>

TouchSensor touchSensor(6,7);  //Connect To Digital
                           // Pin 6 and 7 other to ground

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print("Touch1 = ");
  Serial.println(touchSensor.readTouchSensor1());
  Serial.print("Touch2 = ");
  Serial.println(touchSensor.readTouchSensor2());
  delay(2000);
}
