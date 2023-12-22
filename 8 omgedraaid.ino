// pinnummers instellen
const int LED1 = 2;
const int LED2 = 3;
const int RPICONNECTOR = 8;

// De setup functie 
void setup() {
  // Stel de pinmodus in voor de LED's en de Raspberry Pi connector als OUTPUT
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(RPICONNECTOR, OUTPUT);
}

// De loop functie 
void loop() {
  // status van de RPI_CONNECTOR pin
  boolean connectorState = digitalRead(RPICONNECTOR);

  // Stel de status van de LED's in 
  digitalWrite(LED1, connectorState ? HIGH : LOW);
  digitalWrite(LED2, connectorState ? LOW : HIGH);
}
