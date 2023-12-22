// pinnummers instellen
const int BUTTON1 = 2;
const int RPICONNECTOR = 8;

// status button
boolean buttonState = false;

// De setup functie 
void setup() {
  // Stel de pinmodus in
  pinMode(BUTTON1, INPUT);
  pinMode(RPICONNECTOR, OUTPUT);

  // Start de seriële communicatie
  Serial.begin(9600);
}

// De loop functie
void loop() {
  // Lees de staat van de knop
  boolean currentButtonState = digitalRead(BUTTON1);

  // Controleer of de knopstatus is veranderd naar ingedrukt
  if (currentButtonState && !buttonState) {
    buttonState = true;

    // Wissel de staat van de RPI_CONNECTOR
    digitalWrite(RPICONNECTOR, !digitalRead(RPICONNECTOR));
  } 
  // Controleer of de knop niet meer ingedrukt is
  else if (!currentButtonState) {
    buttonState = false; 
  }
}
