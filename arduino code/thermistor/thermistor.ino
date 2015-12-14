//https://learn.adafruit.com/system/assets/assets/000/000/570/medium800/temperature_thermistor_bb.png?1396764132
//Version 0.1
// Roni Segoly roni@yozma.net
// Date       : 12/12/15
// main code for reading water temperature sensors 
// The code outputs data read for various sensors through Serial port in json format 
// I2C - Messages are also displayed on 16X2 LCD screen https://ryanteck.uk/displays/11-16x2-character-i2c-lcd-display-0635648607139.html?variant=751997007
// needs 10k resistors 

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

// the value of the 'other' resistor
#define SERIESRESISTOR 10000    
#define THERMISTORNOMINAL 10000      
#define BCOEFFICIENT 3950
#define TEMPERATURENOMINAL 25   
 
// What pin to connect the sensor to
#define THERMISTORPIN A0
#define NUMSAMPLES 5

int samples[NUMSAMPLES];
 const int chipSelect = 4;

void setup(void) 
{
  String buffer;
  Serial.begin(9600);
  Serial.println("Moisture code");  y.init_sd();
//  y.write_to_sd("d.txt","12.5");
  lcd.begin(16,2);   // initialize the lcd for 16 chars 2 lines, turn on backlight
  // Delay for sensors to warm p, not sure it's needed
 //y.read_sd_value("d.txt",buffer);
Serial.println(buffer); 
  delay(5000);
}
 
 
void loop()
{
  float a0=0; 
  String fname="exp1.csv";
  a0 = read_termistor(0);
  float a1=0;
  a1 = read_termistor(1);
  float a2=0;
  a2 = read_termistor(2);
  String dataString="";
  Serial.print("{\"A0\":");
  Serial.print(a0);
  Serial.print(", \"A1\":");
  Serial.print(a1);
  Serial.println("}");
  String message = String(a0)+","+String(a1);
 
  y.write_to_sd_append(fname,message);
  
 
  lcd.setCursor(0,0); 
  lcd.print("0:-----"+String(a0)+"      ");
  lcd.setCursor(0,1); 
  lcd.print("1:-----"+String(a1)+"      "); 
  delay(2000);
}


float read_termistor(int pin) 
{
  
  float reading;
  float average = 0;
 float total = 0; 
 for (int i=0; i< NUMSAMPLES; i++) 
 {
       samples[i]= analogRead(pin);
       total += samples[i];
  }
  average = total / NUMSAMPLES;
  //Serial.print("Analog reading "); 
  //Serial.println(average);
 
  // convert the value to resistance
  average = (1023 / average)  - 1;
  average = SERIESRESISTOR / average;
  //Serial.print("Thermistor resistance "); 
  //Serial.println(average);


  float steinhart;
  steinhart = average / THERMISTORNOMINAL;     // (R/Ro)
  steinhart = log(steinhart);                  // ln(R/Ro)
  steinhart /= BCOEFFICIENT;                   // 1/B * ln(R/Ro)
  steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15); // + (1/To)
  steinhart = 1.0 / steinhart;                 // Invert
  steinhart -= 273.15;                         // convert to C
 
  //Serial.print("Temperature "); 
  //Serial.print(steinhart);
  //Serial.println(" *C");
  return (steinhart);
   }
