/* Developed by Spikee */
int enter=0;
void setup()
{
  pinMode(9,INPUT);
  Serial.begin(9600);
}
  void loop()

{
  int c,i,count=0,rpm,v;
  for(i=0;i<=1200;++i)
  {
    c=analogRead(9);
    if(c<400)
    {
      enter=1;
      
    }
    if((c>400)&&(c>v)&&(enter==1))
    {
      count++;
      enter=0;
    }
    delay(22);
    v=c;
  }
  rpm=count*2;
  Serial.println(rpm);
  
}

