#define TRIG 8
#define ECHO 9

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(TRIG,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG,LOW);
  int dur = pulseIn(ECHO,HIGH);
  float dis = (float) dur * 0.17;
  Serial.print(dis);
  Serial.println("mm");
  delay(300);
}
