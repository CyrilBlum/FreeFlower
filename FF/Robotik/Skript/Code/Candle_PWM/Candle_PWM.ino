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
  // Adding a baseline ensures the LEDs stay baseline bright and don't dim completely out.
  baseline = 135; // Minimum brightness level
  random_range = 120; // Range of random brightness variation
  analogWrite(9, random(random_range) + baseline);
  analogWrite(10, random(random_range) + baseline);
  analogWrite(11, random(random_range) + baseline);

  // Pause for a random fraction of a second to create organic flickering
  delay(random(100));
}