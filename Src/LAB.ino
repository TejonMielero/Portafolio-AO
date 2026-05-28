
int pinLuzAnalog = 34;
int pinLuzDigital = 25;
int pinVoltajeAnalog = 32;
int pinHallAnalog = 36;
int pinHallDigital = 13;
int IN1 = 19; int IN2 = 21; int IN3 = 22; int IN4 = 23;

void setup() {
  Serial.begin(115200);
  pinMode(pinLuzDigital, INPUT);
  pinMode(pinHallDigital, INPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
}

void stepMotor(int step) {
  switch(step) {
    case 0: digitalWrite(IN1,HIGH); digitalWrite(IN2,LOW);  digitalWrite(IN3,LOW);  digitalWrite(IN4,LOW); break;
    case 1: digitalWrite(IN1,LOW);  digitalWrite(IN2,HIGH); digitalWrite(IN3,LOW);  digitalWrite(IN4,LOW); break;
    case 2: digitalWrite(IN1,LOW);  digitalWrite(IN2,LOW);  digitalWrite(IN3,HIGH); digitalWrite(IN4,LOW); break;
    case 3: digitalWrite(IN1,LOW);  digitalWrite(IN2,LOW);  digitalWrite(IN3,LOW);  digitalWrite(IN4,HIGH); break;
  }
}

void loop() {
 
  int luzA = analogRead(pinLuzAnalog);
  int voltA = analogRead(pinVoltajeAnalog);
  int hallD = digitalRead(pinHallDigital);

  
  if (hallD == HIGH) {

    for(int i=0; i<200; i++) { 
      stepMotor(i % 4);
      delay(5);
    }
  }

  Serial.print(luzA); Serial.print(",");
  Serial.print(voltA); Serial.print(",");
  Serial.println(hallD);

  delay(300);
}