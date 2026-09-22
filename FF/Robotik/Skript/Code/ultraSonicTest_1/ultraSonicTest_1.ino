#include <USSensor.h>
                           //The Mode Pin (yellow) of SRF05 is connected
USSensor usSensor(10);     //  to Ground. Connect to digital Pin 10 (brown)

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  unsigned long ultraschallWert =  usSensor.readSensorValue();
  Serial.print("Ultraschall = ");
  Serial.print(ultraschallWert);
  Serial.println(" cm");
  delay(1000);
}
