const int potentiometerPin = A0;
const int ledPin = 9;

void setup()
{
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // Convert the 10-bit ADC value to the 8-bit PWM range.
  int sensorValue = analogRead(potentiometerPin);
  int brightness = map(sensorValue, 0, 1023, 0, 255);

  analogWrite(ledPin, brightness);
  delay(10);
}
