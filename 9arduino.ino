#include <IRremote.h>

// pin instellen
const int infraRPin = 2;

// deze pinnen zijn verbonenen met raspberry pi
const int raspberryPiPins[] = {8, 9, 10, 11};

// Initialiseer de IR-ontvanger
IRrecv irrecv(infraRPin);
decode_results results;

// Setup-functie voor het initialiseren van seriële communicatie en IR-ontvanger
void setup(){
  Serial.begin(9600);  // Start seriële communicatie
  irrecv.enableIRIn(); // Activeer de IR-ontvanger
}

//  uitlezen van IR signalen
void loop(){
  // Controleer of er een signaal ontvangen is
  if (irrecv.decode(&results)){
    Serial.println(results.value); // Print de waarde 
    readButtons(results.value);    // Verwerken
    delay(50);                      //  pauze
    irrecv.resume();               // Hervat het ontvangen van IR-signalen
  }
}

// Functie om de signaalwaarde om te zetten 
void readButtons(int value){
  switch(value){
    case 3758596967: sendSignal(0); break;
    case 2257307935: sendSignal(1); break;
    case 2859657027: sendSignal(2); break;
    case 3574811299: sendSignal(3); break;
  }
}

// Functie om signalen naar de Raspberry Pi pinnen te sturen
void sendSignal(int i){
  digitalWrite(raspPins[i], HIGH); // Zet de gekozen pin aan
  delay(50);                       // pauze
  digitalWrite(raspPins[i], LOW);  // Zet de pin uit
}
