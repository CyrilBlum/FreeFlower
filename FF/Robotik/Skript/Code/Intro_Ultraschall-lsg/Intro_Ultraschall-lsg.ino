const int TRIG_PIN = 7;
const int ECHO_PIN = 6;
unsigned long duration;
float distance_cm;

void setup()
{
    Serial.begin(9600);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
}

void loop()
{
    // Trigger auf LOW setzen, damit der Sensor bereit ist
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    // Messung auslösen
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Zeit in Zwischen Signal und Echo in Mikrosekunden
    duration = pulseIn(ECHO_PIN, HIGH);
    Serial.print("duration = ");
    Serial.print(duration);
    Serial.println(" Mikrosekunden");

    // Distanz aus der Zeit berechnen
    distance_cm = duration / 58.0;

    if ((distance_cm > 2) && (distance_cm < 300))
    {
        Serial.print("distance = ");
        Serial.print(distance_cm);
        Serial.println(" cm");
    }
    else
    {
        Serial.println("nicht im Messbereich.");
    }
    delay(500);
}