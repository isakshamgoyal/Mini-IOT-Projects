void setup()
{
  Serial1.begin(115200);
  Serial.begin(9600);                              // the GPRS baud rate
  delay(1000);
}
void loop()
{
  if (Serial.available())
    switch (Serial.read())
    {
      case 't': SendTextMessage();
        break;
      case 'r': ReceiveTextMessage();
        break;
      case 'd': DialVoiceCall();
        break;
      case 'a': AnswerVoiceCall();
        break;
    }
  if (Serial1.available())
    Serial.write(Serial1.read());
}

void AnswerVoiceCall()
{
  Serial1.println("ATA");
}

void SendTextMessage()
{
  Serial1.print("AT+CMGF=1\r"); //Because we want to send the SMS in text mode
  delay(1000);

  Serial1.println("AT+CMGS=\"+918571025320\"");
  delay(1000);

  Serial1.println("Hello from the other side! Bhaap");
  delay(1000);

  Serial1.println((char)26); //the ASCII code of the ctrl+z is 26 (0x1A)
  delay(1000);

  Serial1.println();
}

void ReceiveTextMessage()
{
  Serial1.println("AT+CMGF=1"); //Because we want to receive the SMS in text mode
  delay(1000);

  Serial1.println("AT+CPMS=\"SM\""); // read first SMS
  delay(1000);

  Serial1.println("AT+CMGL=\"ALL\""); // show message
}


void DialVoiceCall()
{
  Serial1.println("ATD + 918571025320;");//dial the number
  delay(100);
  Serial1.println();
}

void ShowSerialData()
{
  while (Serial1.available() != 0)
    Serial.write(Serial1.read());
}



