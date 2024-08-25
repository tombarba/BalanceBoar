/*
  Arduino LSM9DS1 - Simple Gyroscope

  This example reads the gyroscope values from the LSM9DS1
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.

  The circuit:
  - Arduino Nano 33 BLE Sense

  created 10 Jul 2019
  by Riccardo Rizzo

  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>

unsigned long t ;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.print("Magnetometer sample rate = ");
  Serial.print(IMU.magneticFieldSampleRate());
  Serial.println(" Hz");

}

void loop() {
  float Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz;

  t = millis();

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(Ax, Ay, Az);}
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(Gx, Gy, Gz);}
  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(Mx, My, Mz);}

    Serial.print(t);
    Serial.print('\t');
    Serial.print(Ax);
    Serial.print('\t');
    Serial.print(Ay);
    Serial.print('\t');
    Serial.print(Az);

    Serial.print('\t');
    Serial.print(Gx);
    Serial.print('\t');
    Serial.print(Gy);
    Serial.print('\t');
    Serial.print(Gz);

    Serial.print('\t');
    Serial.print(Mx);
    Serial.print('\t');
    Serial.print(My);
    Serial.print('\t');
    Serial.println(Mz);
  
}
