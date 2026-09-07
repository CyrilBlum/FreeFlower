const int ldrPin = A0;
const int ledPin = 13;
const int threshold = 512;

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int sensorValue = analogRead(ldrPin);
  Serial.println(sensorValue);

  if (sensorValue > threshold) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(50);
}
