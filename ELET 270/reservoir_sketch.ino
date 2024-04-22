#include <CapacitiveSensor.h>

CapacitiveSensor cs = CapacitiveSensor(4, 2);

void setup(){
  cs.set_CS_AutocaL_Millis(0xFFFFFFFF);
  Serial.begin(9600);
  }
  
void loop(){
  long reading = cs.capacitiveSensor(30);
  Serial.println(reading);
  delay(10);
  }