#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotorRechts = AFMS.getMotor(1);
Adafruit_DCMotor *myMotorLinks = AFMS.getMotor(2);

void setup()
{
  AFMS.begin();
  myMotorLinks->run(RELEASE);
  myMotorRechts->run(RELEASE);
  myMotorLinks->setSpeed(30);
  myMotorRechts->setSpeed(30);
  myMotorLinks->run(FORWARD);
  myMotorRechts->run(FORWARD);
  delay(5000);

  myMotorLinks->setSpeed(100);
  myMotorRechts->setSpeed(50);
  myMotorLinks->run(FORWARD);
  myMotorRechts->run(FORWARD);
  delay(1000);
  myMotorLinks->run(RELEASE);
  myMotorRechts->run(RELEASE);
}

void loop()
{
}
