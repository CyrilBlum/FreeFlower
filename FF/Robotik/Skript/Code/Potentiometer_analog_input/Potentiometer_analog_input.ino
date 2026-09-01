int sensorValue = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
}

void loop()
{
  // Read the analog input on pin A0.
  // The value will be between 0 and 1023.
  // sensorValue is a 10-bit value d, which is the resolution of 
  // the ADC (Analog-to-Digital Converter) on the Arduino.
  sensorValue = analogRead(A0);

  Serial.println(sensorValue);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(sensorValue);

  digitalWrite(LED_BUILTIN, LOW);
  delay(sensorValue);
}