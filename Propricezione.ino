/*
- https://www.arduino.cc/reference/en/#functions
*/

#include <Arduino_LSM9DS1.h>
#include <cmath>

void sample(float& Ax, float& Ay, float& Az, float& Gx, float& Gy, float& Gz, float&  Mx, float& My, float& Mz);
float deg2rad(float degrees);
float rad2deg(float radians);
void printIMU(float Ax, float Ay, float Az, float Gx, float Gy, float Gz, float Mx, float My, float Mz);
void roll(float& roll_A, float& roll_G, float& roll_C);

unsigned long t_old ;
unsigned long t ;
float dt ;

const float alpha = 0.02;

float Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz;

float roll_A,roll_G,roll_C;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  /*
  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.print("Magnetometer sample rate = ");
  Serial.print(IMU.magneticFieldSampleRate());
  Serial.println(" Hz");
  */

  //t_old = ((float)millis())/1000.0;

}

void loop() {
  
  t_old = ((float)micros());///1000.0;
  

  sample(Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz);

  //printIMU(Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz);

  //Serial.print("t_old:");
  //Serial.println(t_old/1000000.0);
  //Serial.print("t:");
  //Serial.println(t/1000000.0);
  //Serial.print("dt:");
  //Serial.println((t-t_old)/1000000.0);
  //Serial.print("\tGz:");
  //Serial.println(Gz);
    
  roll(roll_A, roll_G, roll_C);
  
  printRoll(roll_A, roll_G, roll_C);

  t = ((float)micros());///1000.0;

  dt = float(t-t_old)/1000000.0; // not sure
  //t_old = t;
  
}

void roll(float& roll_A, float& roll_G, float& roll_C){
  roll_A = rad2deg(atan2(Ay, Ax)); // rad
  roll_G = roll_G + Gz*dt; //rad/s * s
  roll_C = (1-alpha)*(roll_C + Gz*dt)+ alpha*roll_A;
}

void printRoll(float roll_A, float roll_G, float roll_C){
    //Serial.print(t);
    Serial.print("A:");
    Serial.print(roll_A);
    Serial.print("\tG:");
    Serial.print(roll_G);
    Serial.print("\tC:");
    Serial.println(roll_C);
    }

void sample(float& Ax, float& Ay, float& Az, float& Gx, float& Gy, float& Gz, float&  Mx, float& My, float& Mz){
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(Ax, Ay, Az);}
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(Gx, Gy, Gz);}
  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(Mx, My, Mz);
    
    //Gx = deg2rad(Gx);
    //Gy = deg2rad(Gy);
    //Gz = deg2rad(Gz);
    }
    
}

void printIMU(float Ax, float Ay, float Az, float Gx, float Gy, float Gz, float Mx, float My, float Mz){

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

float deg2rad(float degrees){

  return (degrees * 71.0) / 4068.0;
}

float rad2deg(float radians){

  return (radians * 4068.0) / 71.0;
}
