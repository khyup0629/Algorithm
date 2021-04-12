#define ENA 5
#define IN1 6
#define IN2 7

void setup() {
  // put your setup code here, to run once:
  //pinMode(ENA,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //digitalWrite(ENA,HIGH);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
}
