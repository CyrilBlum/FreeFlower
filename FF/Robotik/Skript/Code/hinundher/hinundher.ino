#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
#include <USSensor.h>

const int SENSOR_PIN = 10;

const int SPEED = 20;
const int ROTATION_TIME = 1800; // muss kalibriert werden
const int MIN_DISTANCE_CM = 10;
const int ANZAHL_DREHUNGEN = 5;

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
    Serial.begin(9600);
    AFMS.begin();
    stoppen();

    unsigned long distanceCm;
    int i = 0;

    while (i < ANZAHL_DREHUNGEN)
    {
        Serial.print("Distanz = ");
        Serial.print(distanceCm);
        Serial.println(" cm");
        distanceCm = usSensor.readSensorValue();
        if (distanceCm <= MIN_DISTANCE_CM)
        {
            stoppen();
            drehenAnOrt(SPEED);
            i += 1;
        }
        else
        {
            vorwaertsFahren(SPEED);
        }

        delay(100);
    }
    stoppen();
}

void loop()
{ // do nothing
}