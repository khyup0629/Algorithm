# SHA(Secure Hash Algorithm) 알고리즘

+ 1993년 미국 국가안보국(NSA)의 설계를 시작으로 SHA 함수군에 속하는 최초의 함수는 공시적으로 SHA라고 불렸지만 나중에 설계된 함수들과 구별하기 위하여 SHA-0이라고 불리고 있다.
+ 가장 처음으로 발표된 SHA-0을 기점으로 SHA-1과 SHA-2 계열이 있으며 가장 나중에 SHA-3 알고리즘이 공개되었다.
+ 2년 후인 1995년 SHA-0의 변형인 SHA-1이 나왔으며, 이후 변형을 통해 4종류가 추가로 공개되었다.
+ 통칭 SHA-2로 불리는 변형 4종에는 SHA-224, SHA-256, SHA-384, SHA-512가 있다.

+ [SHA-256](#SHA-256)
+ [SHA-512](#SHA-512)

## SHA-256

> <h3>개요

+ SHA(Secure Hash Algorithm) 알고리즘의 한 종류로서 256비트로 구성되며 64자리(4비트 당 1자리) 문자열을 반환한다.
+ 미국의 국립표준기술연구소(NIST)에 의해 공표된 표준 해시 알고리즘인 SHA-2 계열 중 하나이다.
+ **블록체인**에서 가장 많이 채택하여 사용하고 있다.
+ 어떤 길이의 값을 입력하더라도 256비트의 고정된 결괏값을 출력한다.
	+ 일반적으로 입력값이 조금만 변동하여도 출력값이 완전히 달라지기 때문에 출력값을 토대로 입력값을 유추하는 것은 거의 불가능하다.
	+ 아주 작은 확률로 입력값이 다름에도 불구하고 출력값이 같은 경우가 발생하는데 이것을 **충돌**이라고 한다.
	+ 이러한 **충돌**의 발생 확률이 낮을수록 좋은 함수라고 평가된다.

> <h3>특징

+ 현재 **블록체인**에서 가장 많이 채택하여 사용되고 있는 암호 방식이다.
+ 단방향성의 성질을 띄고 있는 암호화 방법으로 **복호화가 불가능**하다.
	+ **복호화** : 부호화의 반댓말로 출력값을 토대로 역으로 입력값을 알아내는 것을 말한다.
+ **안정성이 상당이 우수**하며 속도가 빨라 상용화가 잘 되어있다.
+ 데이터의 수정과 변경을 검출 할 수 있으나 **인증은 불가능**하다.

## SHA-512

> <h3>개요

+ SHA(Secure Hash Algorithm) 알고리즘의 한 종류로서 512비트로 구성되며 128자리(4비트 당 1자리) 문자열을 반환한다.
+ 미국의 국립표준기술연구소(NIST)에 의해 공표된 표준 해시 알고리즘인 SHA-2 계열 중 하나이다.
+ 2001년에 미국 국가안보국은 SHA-2를 개발했으며 2002년에 표준으로 제정되었다. 
+ SHA-512는 46~80 라운드를 통과해야 공격으로부터 안전하다고 판단하며, 1024 비트(bit)를 1개의 패딩 메시지로 만든다.

> <h3>특징

+ **512비트**의 해시값을 생성한다.
+ 일반적으로 길이가 **128자리**인 **16진수**로 렌더링된다.
+ PRNG의 출력이나 랜덤 패딩에 대해 **가능한 많이 출력이 필요한 경우**에 대해 강점을 갖고 있다.

> <h3>패딩

+ SHA-512의 전체적인 진행과정 중 가장 처음으로 발생하는 과정이다.
+ 패딩은 100개의 공간에 문자 1개가 들어오면 나머지 99개의 공간을 숫자 0 등으로 메우는 작업이다.
+ 1024비트를 1개의 패딩 메시지로 형성한다.
+ 1개의 패딩 메시지는 입력으로 준 메시지와 메시지의 끝, 0으로 된 패딩 값, 메시지의 길이와 같은 다양한 정보가 포함된다.

> <h3>파싱

+ 해시 함수의 연산을 진행하기 전에 선행되는 과정이다.
+ 컴퓨터에서 컴파일러 또는 번역기가 원시 부호를 기계어로 번역하는 과정의 한 단계로, 각 문장의 문법적인 구성 또는 구문을 분석하는 과정이다.
+ SHA-512에서 패딩된 메시지의 파싱은 N개의 1024비트 덩어리의 패딩 메시지가 존재한다.

> <h3>단점

+ SHA-256이 SHA-512보다 훨씬 빠르게 64개의 해시를 만들어낸다. 즉, **아직까지 SHA-512를 사용할 만큼의 문제점도 발견되지 않았다.**
+ 현재에는 짧은 문자열(36 ~ 49 문자)이 사용되고 있고 긴 문자열(72 ~ 85 문자)에서도 **큰 속도의 차이는 없기 때문에 상대적으로 느리며, 기술 비용이 많이 들어가는 SHA-512를 채택할 필요는 없다.**
+ SHA-512의 특성상 결과 값이 512비트로만 나와서 용량(공간)을 너무 많이 차지한다

> <h3>SHA-256과의 차이점(현재로서 이해되지 않음)

+ 블록의 크기는 1024비트로 변경
+ 초기 해시 값 및 라운드 상수는 64비트로 확장
+ 라운드(과정)는 62라운드가 아닌 80라운드로 변경
+ 메시지 스케줄 배열은 64개의 32비트 문자 대신 80개의 64비트의 문자를 갖게 된다
+ 메시지 스케줄 배열을 확장하기 위해 루프는 16개에서 63개로 확장시키는 것이 아니라 16개에서 79개로 확장 시킨다.
+ 원형 상수는 처음 80개의 소수에 기초한다 2.409
+ 계산에 사용되는 단어 크기는 64비트이다.
+ 메시지의 추가 길이 (전처리 전)는 비트 단위로 128비트 빅 엔디안 정수를 갖는다.
+ 사용된 이동 및 회전 양이 다르다.
