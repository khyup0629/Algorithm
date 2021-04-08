#include <SoftwareSerial.h>

SoftwareSerial btSerial(12,13);//(RX,TX)=(12,13)
#define ENA 5 // analog
#define IN1 6 // digital
#define IN2 7 // digital
#define TRIG 8 // digital
#define ECHO 9 // digital

void setup() {
  Serial.begin(9600);
  btSerial.begin(9600); // 소프트웨어 시리얼 통신 설정
  pinMode(TRIG,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(ENA,OUTPUT);
}

void loop() {
  if(btSerial.available()) //Serial.available()은 시리얼버퍼를 검사
  {
    char order = btSerial.read(); //Serial.read()은 시리얼버퍼에 있는 데이터를 읽어들임
    switch(order)
    {
      case 'o': //o인경우 문열기
      digitalWrite(IN1,HIGH);
      digitalWrite(IN2,LOW);
      analogWrite(ENA,255);
      delay(1000); // door open time 고치기
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,LOW);
      break;
      case 'c': //c인경우 문닫기
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,HIGH);
      analogWrite(ENA,255);
      delay(1000); // door close time 고치기
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,LOW);
      break;
      default:
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,LOW);
    }
  }
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
      delay(1000); // door open time 고치기
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
          delay(1000); // door close time 고치기
          analogWrite(ENA,0); // door stop
          break; // out of while{}
        }
        delay(4000); // 4초마다 거리 측정
      }
    }
    delay(4000); //타협
}
