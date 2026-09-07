#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield motorShield = Adafruit_MotorShield();
Adafruit_DCMotor *rightMotor = motorShield.getMotor(1);
Adafruit_DCMotor *leftMotor = motorShield.getMotor(2);

void setup()
{
  motorShield.begin();
  leftMotor->run(RELEASE);
  rightMotor->run(RELEASE);
  leftMotor->setSpeed(30);
  rightMotor->setSpeed(30);
  leftMotor->run(FORWARD);
  rightMotor->run(FORWARD);
  delay(5000);

  leftMotor->setSpeed(100);
  rightMotor->setSpeed(50);
  delay(1000);
  leftMotor->run(RELEASE);
  rightMotor->run(RELEASE);
}

void loop()
{
}
