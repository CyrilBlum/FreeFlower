#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
#include <USSensor.h>

const int SENSOR_PIN = 10;

const int SPEED = 20;
const int ROTATION_TIME = 1800; // muss kalibriert werden
const int MIN_DISTANCE_CM = 10;
const int MAX_ANZAHL_DREHUNGEN = 5;

USSensor usSensor(SENSOR_PIN);

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motorRechts = AFMS.getMotor(1);
Adafruit_DCMotor *motorLinks = AFMS.getMotor(2);

void vorwaertsFahren(int speed)
{
    motorLinks->setSpeed(speed);
    motorRechts->setSpeed(speed);

    motorLinks->run(FORWARD);
    motorRechts->run(FORWARD);
}

void stoppen()
{
    motorLinks->run(RELEASE);
    motorRechts->run(RELEASE);
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

void setup()
{
    AFMS.begin();
    stoppen();

    unsigned long distanceCm;
    int anzahl_drehungen = 0;

    while (anzahl_drehungen < MAX_ANZAHL_DREHUNGEN)
    {
        // Hier kommt Ihr Code hin.

        delay(100);
    }
    stoppen();
}

void loop()
{ // do nothing
}