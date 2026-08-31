// Realistic Candle Light Effect
// Source: Carlos Pineiro (YouTube: uX9YMCLgK9A)

void setup() {
  // Configure the three PWM pins as outputs
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // Set a random brightness level for each LED.
  // Adding 135 ensures the LEDs stay baseline bright and don't dim completely out.
  analogWrite(9, random(120) + 135);
  analogWrite(10, random(120) + 135);
  analogWrite(11, random(120) + 135);
  
  // Pause for a random fraction of a second to create organic flickering
  delay(random(100));
}