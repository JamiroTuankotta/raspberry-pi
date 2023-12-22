// de pinnummers instellen
const int LED_1 = 13;
const int LED_2 = 12;

// array voor twee LED-pinnen
const int led[] = {8, 9};

// De setup functie 
void setup() {
  // Stel de pinmodus in voor de LED pinnen als OUTPUT
  pinMode(led[0], OUTPUT);
  pinMode(led[1], OUTPUT);

  // Stel de pinmodus in voor de Raspberry Pi LED-pinnen als INPUT
  pinMode(LED_1, INPUT);
  pinMode(LED_2, INPUT);
}

// De loop-functie wordt herhaaldelijk uitgevoerd
void loop() {
  // Lees de status 
  if(digitalRead(LED_1)) {
    // Als led 1 HIGH is, zet dan de eerste LED aan en de tweede uit
    digitalWrite(led[0], HIGH);
    digitalWrite(led[1], LOW);
  } else {
    // Als led 1 LOW is, doe het tegenovergestelde
    digitalWrite(led[0], LOW);
    digitalWrite(led[1], HIGH);
  }
}
