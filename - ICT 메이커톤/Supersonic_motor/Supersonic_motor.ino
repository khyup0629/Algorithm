#define ENA 5 // analog
#define IN1 6 // digital
#define IN2 7 // digital
#define TRIG 8 // digital
#define ECHO 9 // digital

void setup() {
  Serial.begin(9600);
  pinMode(TRIG,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
}

void loop() {
  digitalWrite(TRIG,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG,LOW);
  int dur = pulseIn(ECHO,HIGH);
  float dis = (float) dur * 0.170;
  Serial.print(dis);
  Serial.println("mm");

  if (dis <= 200){ // drone come
    analogWrite(ENA,255); // door open
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    delay(2000); // door open time
    while (1){
      digitalWrite(TRIG,HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIG,LOW);
      int dur = pulseIn(ECHO,HIGH);
      float dis = (float) dur * 0.170;
      Serial.print(dis);
      Serial.println("mm");
      if (dis <= 200){ // still inner 200m 
        analogWrite(ENA,0); // door stop
      }
      else{ // drone gone
        analogWrite(ENA,255); // door close
        digitalWrite(IN1,LOW);
        digitalWrite(IN2,HIGH);
        delay(2000); // door close time
        analogWrite(ENA,0); // door stop
        break; // out of while{}
      }
      delay(7000); // 7초마다 거리 측정
    }
  }
  delay(7000); // 7초마다 거리 측정
}
