#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
#include <USSensor.h>

const int SENSOR_PIN = 10;
const int SPEED = 20;

// Diese Zeit müssen Sie experimentell so einstellen,
// dass der Roboter ungefähr 10° dreht.
const int ROTATION_TIME = 200;

USSensor usSensor(SENSOR_PIN);

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motorRechts = AFMS.getMotor(1);
Adafruit_DCMotor *motorLinks = AFMS.getMotor(2);

void stoppen()
{
    motorLinks->setSpeed(0);
    motorRechts->setSpeed(0);
}

void drehenAnOrt(int speed)
{
    motorLinks->setSpeed(speed);
    motorRechts->setSpeed(speed);

    motorLinks->run(FORWARD);
    motorRechts->run(BACKWARD);

    delay(ROTATION_TIME);

    stoppen();
}
void experiment()
{
    int angle = 0;
    Serial.println("starting experiment");
    while (angle < 360)
    {

        // Distanz messen
        unsigned long distanceCm = usSensor.readSensorValue();

        // Ausgabe der Messwerte
        Serial.print(distanceCm);
        Serial.println(",");
        delay(200);

        // ungefähr 10° drehen
        drehenAnOrt(SPEED);

        delay(300);

        angle += 10;
    }

    stoppen();
}

void setup()
{
    Serial.begin(9600);
    AFMS.begin();

    stoppen();

    delay(1000);
}

void loop()
{
    // Das Experiment wird gestartet
    // wenn man über den Serial Monitor
    // ein "s" an den Arduino sendet
    if (Serial.available() > 0)
    {
        char command = Serial.read();

        if (command == 's')
        {
            experiment();
        }
    }
}