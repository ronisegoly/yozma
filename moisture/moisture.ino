//https://learn.adafruit.com/system/assets/assets/000/000/570/medium800/temperature_thermistor_bb.png?1396764132
#include <SPI.h>
#include <SD.h>
#include <Wire.h>  // Comes with Arduino IDE
#include <OneWire.h>
#include <LiquidCrystal_I2C.h>
#include "DHT.h"
#include <stdio.h>
#include "yozma.h"

/*
 SD circuit:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 10
*/

Yozma y(1); //set 0 for no debug print, 1 with debug print

//DEFINING LCD I2C
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address


int i=0;
void setup() 
{
  String buffer;
  Serial.begin(9600);
  y.init_sd();
  //  y.write_to_sd("d.txt","12.5");
  lcd.begin(16, 2);  // initialize the lcd for 16 chars 2 lines, turn on backlight
  // Delay for sensors to warm p, not sure it's needed
  //y.read_sd_value("d.txt",buffer);
  lcd.begin(16,2);   // initialize the lcd for 16 chars 2 lines, turn on backlight
   Serial.println(buffer);
  delay(5000);
}
 
 
void loop() 
{
    int moisture0 = analogRead(0);
    moisture0=1000-moisture0;
    if (moisture0<0)
      moisture0=0;
    delay(1000);
    
    int moisture1 = analogRead(1);
    moisture1=1000-moisture1;
    if (moisture1<0)
      moisture1=0;
    delay(1000);
    
    int moisture2 = analogRead(2);
    moisture2=1000-moisture2;
    if (moisture2<0)
      moisture2=0;
    delay(1000);
    
    int moisture3 = analogRead(3);
    moisture3=1000-moisture3;
    if (moisture3<0)
      moisture3=0;
    delay(1000);
    
    int mil=random(0,1000);
    if (mil>10000)
      mil=0;
    String fname = "exp1.csv";
    Serial.print("{\"A0\":");
    Serial.print(moisture0);
    Serial.print(", \"A1\":");
    Serial.print(moisture1);
    Serial.print(", \"A2\":");
    Serial.print(moisture2);
    Serial.print(", \"A3\":");
    Serial.print(moisture3);
    Serial.print(", \"RAND\":");
    Serial.print(mil);
    Serial.println("}");
    String message = String(moisture0) + "," + String(moisture1)+","+String(moisture2)+","+String(moisture3);
    y.write_to_sd_append(fname, message);
    lcd.setCursor(0,0); 
    lcd.print("               ");
    lcd.setCursor(0,0); 
    lcd.print("0:"+String(moisture0)+"    1:"+String(moisture1));
    lcd.setCursor(0,1); 
    lcd.print("                ");
    lcd.setCursor(0,1); 
    lcd.print("2:"+String(moisture2)+"    3:"+String(moisture3));
    delay(5000);
}

