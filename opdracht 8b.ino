// pinnummers instellen
const int LED1 = 13;
const int LED2 = 12;

//  array voor twee LED-pinnen
const int led[] = {8, 9};

// De setup functie 
void setup() {
  // Stel de pinmodus in voor de LED-pinnen als OUTPUT
  pinMode(led[0], OUTPUT);
  pinMode(led[1], OUTPUT);

  // Stel de pinmodus in voor de Raspberry Pi LED-pinnen als INPUT
  pinMode(LED1, INPUT);
  pinMode(LED2, INPUT);
}

// De loop functie 
void loop() {
  // Lees de status van LED 1 en pas de status van de eerste LED aan
  digitalWrite(led[0], digitalRead(LED1) ? HIGH : LOW);

  // Lees de status van LED 2 en pas de status van de tweede LED aan
  digitalWrite(led[1], digitalRead(LED2) ? HIGH : LOW);
}
