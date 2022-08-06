/* Developed by Spikee */ 
const int motor1Pin1 = 12;
const int motor1Pin2 = 10;
const int motor2Pin1 = 4;
const int motor2Pin2 = 2;
byte serialA;


  int vSpeed=255;   // Default speed, from 0 to 255
  int v=230;//adjust according to requirement to get sharp turns

void setup() {
    // Set pins as outputs:
    pinMode(motor1Pin1, OUTPUT);
    pinMode(motor1Pin2, OUTPUT);
    pinMode(motor2Pin1, OUTPUT);
    pinMode(motor2Pin2, OUTPUT);
    // Initialize serial communication.
    Serial.begin(9600);
}
 
void loop() {
    if(Serial.available() > 0)
    {
      serialA = Serial.read();Serial.println(serialA);
    }  
    
     
  switch(serialA){
  //for forward moveent
    case 'F': {
        analogWrite(motor1Pin1, vSpeed);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1, 0);
        analogWrite(motor2Pin2, vSpeed);
       break; 
    }
//turn left
   case 'L': {
        analogWrite(motor1Pin1, vSpeed);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1, v);
        analogWrite(motor2Pin2, 0);

     
    }
break;
  //turn right
   case 'R': {
        analogWrite(motor1Pin1,0);
        analogWrite(motor1Pin2, vSpeed); 
        analogWrite(motor2Pin1, 0);
        analogWrite(motor2Pin2, v);
       
    }
 break;
  //forward left
    case 'G': {
        analogWrite(motor1Pin1, vSpeed);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1, 0);
        analogWrite(motor2Pin2, 0);
       
    }
    break;
  
  //forward right
   case 'I':{
       analogWrite(motor1Pin1, 0);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1,0);
        analogWrite(motor2Pin2, vSpeed);
       
    }
    break;
  //backward
    case 'B': {
     analogWrite(motor1Pin1, 0);
        analogWrite(motor1Pin2,vSpeed); 
        analogWrite(motor2Pin1, vSpeed);
        analogWrite(motor2Pin2, 0);
       
    }
  break;
  //backward left
case 'H': {
        analogWrite(motor1Pin1, vSpeed);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1, v);
        analogWrite(motor2Pin2, 0);
       
    }
    break;
  
  //backward right
    case 'J': {
        analogWrite(motor1Pin1, 0);
        analogWrite(motor1Pin2, vSpeed); 
        analogWrite(motor2Pin1, 0);
        analogWrite(motor2Pin2, vSpeed);
       
    }
    break;
  
      case 'X':
      {
      analogWrite(motor1Pin1, 0);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1,0);
        analogWrite(motor2Pin2, 0);
      }
      break;
       case 'x': {
        analogWrite(motor1Pin1, vSpeed);
        analogWrite(motor1Pin2, 0); 
        analogWrite(motor2Pin1, 0);
        analogWrite(motor2Pin2, vSpeed);

        break; 
      //stop the car
      
      }
}}



