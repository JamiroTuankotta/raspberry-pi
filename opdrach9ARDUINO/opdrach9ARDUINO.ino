#include <IRremote.h>

const int irPin = 2;

const int raspPins[] = {8, 9, 10, 11};

IRrecv irrecv(irPin);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop(){
  // Uitlezen signaal infrarood afstandsbediening
  if (irrecv.decode(&results)){
    Serial.println(results.value);
    readButtons(results.value);
    delay(50);
    irrecv.resume();
  }
}

// Omzetten signaal afstandsbediening van knoppen 1 tot 4 -> zero-indexed cijfer
void readButtons(int value){
  switch(results.value){
    case 3758596967:
    sendSignal(0);
    break;
    case 2257307935:
    sendSignal(1);
    break;
    case 2859657027:
    sendSignal(2);
    break;
    case 3574811299:
    sendSignal(3);
    break;
  }
}

// Schrijven signaal naar pins die verbonden zijn met de Raspberry Pi
void sendSignal(int i){
  digitalWrite(raspPins[i], HIGH);
  delay(50);
  digitalWrite(raspPins[i], LOW);
}