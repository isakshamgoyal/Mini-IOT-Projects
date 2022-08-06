void setup() {
  //Set pin 12 as output
  pinMode(12, OUTPUT);
  //GSM power on sequence
  digitalWrite(12, HIGH);
  delay(2000);
  digitalWrite(12, LOW);
}

void loop() {
}
