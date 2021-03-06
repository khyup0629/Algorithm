[뒤로](https://github.com/khyup0629/Algorithm)

---
# KMP 알고리즘

+ 문자열을 검색함에 있어 빠르게 검색하기 위한 문자열 검색 알고리즘이다.
+ 비교할 필요가 없는 부분을 찾아 그 부분을 뛰어넘어 여러 칸을 이동하면서 계산 시간을 빠르게 할 수 있다.

> <h3>접두부와 접미부

+ 접두부 : 문자열의 앞부분 문자열
+ 접미부 : 문자열의 뒷부분 문자열
+ 예를 들어 **BAABAA** 라는 문자열이 있다고 하자.
+ 이 문자열의 접두부와 접미부의 모든 경우의 수는 아래와 같다.

![image](https://user-images.githubusercontent.com/43658658/117923739-8f10a680-b32f-11eb-9104-071fdc29a26a.png)

+ KMP 알고리즘은 **접두부와 접미부가 같은 부분 문자열**을 이용한다.

> <h3>KMP 알고리즘 동작 방식

+ [문제]전체 문자열 **BABCABABAABABAA** 중에서 **BAABABAA** 문자열을 찾는다고 하자.

![image](https://user-images.githubusercontent.com/43658658/117924791-41953900-b331-11eb-8862-65bb8fdd6138.png)

+ [Step 1] 찾는 문자열을 제일 왼쪽에 놓고 전체 문자열과 비교해 다른 부분을 찾는다.
  + 찾는 문자열 기준으로 **2번 인덱스**에서 다른 문자가 확인되었다.
  + **2번 인덱스 앞부분의 문자열**이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **접두부와 접미부가 같은 경우가 없으므로 길이는 0이다.**

![image](https://user-images.githubusercontent.com/43658658/117925916-e106fb80-b332-11eb-9fde-9203843831e6.png)

+ [Step 2] 찾는 문자열 기준 다른 문자가 확인되는 인덱스 번호(2) - 최대 접두부 길이(0) = 2 만큼 오른쪽으로 이동한다.
  + 찾는 문자열 기준으로 **1번 인덱스**에서 다른 문자가 확인되었다.
  + **1번 인덱스 앞부분의 문자열**이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **접두부와 접미부가 같은 경우가 없으므로 길이는 0이다.**

![image](https://user-images.githubusercontent.com/43658658/117926091-2d523b80-b333-11eb-833e-1e4f14081dca.png)

+ [Step 3] 찾는 문자열 기준 다른 문자가 확인되는 인덱스 번호(1) - 최대 접두부 길이(0) = 1 만큼 오른쪽으로 이동한다.
  + 찾는 문자열 기준으로 **0번 인덱스**에서 다른 문자가 확인되었다.
  + **0번 인덱스 앞부분의 문자열**이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **0번 인덱스 앞의 문자열이 없으므로 최대 접두부 길이를 -1로 한다.**

![image](https://user-images.githubusercontent.com/43658658/117926243-6be7f600-b333-11eb-986a-8d5cc918d9c2.png)

+ [Step 4] 찾는 문자열 기준 다른 문자가 확인되는 인덱스 번호(0) - 최대 접두부 길이(-1) = 1 만큼 오른쪽으로 이동한다.
  + 찾는 문자열 기준으로 **0번 인덱스**에서 다른 문자가 확인되었다.
  + **0번 인덱스 앞부분의 문자열**이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **0번 인덱스 앞의 문자열이 없으므로 최대 접두부 길이를 -1로 한다.**

![image](https://user-images.githubusercontent.com/43658658/117926463-c6815200-b333-11eb-8ffa-9fa10ad6c734.png)

+ [Step 5] 찾는 문자열 기준 다른 문자가 확인되는 인덱스 번호(0) - 최대 접두부 길이(-1) = 1 만큼 오른쪽으로 이동한다.
  + 찾는 문자열 기준으로 **2번 인덱스**에서 다른 문자가 확인되었다.
  + **2번 인덱스 앞부분의 문자열**이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **접두부와 접미부가 같은 경우가 없으므로 길이는 0이다.**

![image](https://user-images.githubusercontent.com/43658658/117926563-eadd2e80-b333-11eb-9b0e-f8e182661f19.png)

+ [Step 6] 찾는 문자열 기준 다른 문자가 확인되는 인덱스 번호(2) - 최대 접두부 길이(0) = 2 만큼 오른쪽으로 이동한다.
  + 찾는 문자열 기준으로 **모든 문자열이 일치**한다. 일치하는 문자열 개수 +1
  + 앞부분의 문자열이 접두부와 접미부가 같은 것이 있을 경우, 접두부 길이가 최대가 될 수 있는 경우를 찾고 접두부 길이를 구한다.
  + 현재 Step의 경우에는 **접두부 BAA, 접미부 BAA가 같고 길이가 최대이므로 최대 접두부 길이는 3이다.**

![image](https://user-images.githubusercontent.com/43658658/117926690-1c55fa00-b334-11eb-9b5e-d15deaeef60c.png)

+ [Step 7] 찾는 문자열의 길이(8) - 최대 접두부 길이(3) = 5 만큼 오른쪽으로 이동한다.

![image](https://user-images.githubusercontent.com/43658658/117927853-c08c7080-b335-11eb-9284-22484cdd671e.png)

+ [Step 8] 전체 문자열을 벗어났으므로 종료한다.

+ [결과] 일치하는 문자열 갯수 : 1개

> <h3>실패 함수

+ 실패 함수는 KMP 알고리즘 수행 중, 일치하지 않는 문자가 있을 때 **어디서부터 검색을 해야 할 지(몇 칸을 뛰어넘어야 할지) 알려주는 지표**이다.
+ **패턴의 처음부터 해당 위치까지 일치하는 접두부와 접미부의 길이가 얼마나 되는지를 기록하는 부분 일치 테이블(pi)을 만드는 함수**이다.
+ **부분 일치 테이블(pi)의 마지막 인덱스 값을 확인**하면 **최대 접두부의 길이**를 알 수 있다.

+ [문제] 최대 접두부의 길이를 찾아야 하는 문자열이 **AABAAA** 라고 하자.
+ pi 테이블의 길이를 문자열 길이만큼으로 만들고 모든 값을 0으로 설정한다.
+ i = 1, j = 0부터 출발한다.

![image](https://user-images.githubusercontent.com/43658658/117929469-d307a980-b337-11eb-8216-3186447c5805.png)

+ [Step 1] 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 같기** 때문에 j를 +1한 후 pi[i] = j 를 기록한다.
  + pi[1] = 1, j = 1

![image](https://user-images.githubusercontent.com/43658658/117929798-2c6fd880-b338-11eb-85ed-63a619bc1a20.png)

+ [Step 2] **i를 +1**하고 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 다르므로** j가 0이 되거나 문자열[i]과 문자열[j]가 같아질 때까지 **j = pi[j-1]를 반복**한다.
  + 반복 결과 j = pi[1-0] = 0 이 되었을 때 **j가 0이 되었으므로 반복이 종료**된다.

![image](https://user-images.githubusercontent.com/43658658/117930304-cc2d6680-b338-11eb-9369-8c747c15356e.png)

+ [Step 3] 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 다르므로** i를 +1한다.

![image](https://user-images.githubusercontent.com/43658658/117930370-dcdddc80-b338-11eb-84e7-3ff29cb0140e.png)

+ [Step 4] 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 같기** 때문에 j를 +1한 후 pi[i] = j 를 기록한다.
  + pi[3] = 1, j = 1

![image](https://user-images.githubusercontent.com/43658658/117930578-20d0e180-b339-11eb-85e2-659579861ad2.png)

+ [Step 5] **i를 +1**하고 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 같기 때문에** j를 +1한 후 pi[i] = j 를 기록한다.
  + pi[4] = 2, j = 2

![image](https://user-images.githubusercontent.com/43658658/117930715-4cec6280-b339-11eb-8266-4e1e6661ce7e.png)

+ [Step 6] **i를 +1**하고 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 다르므로** j가 0이 되거나 문자열[i]과 문자열[j]가 같아질 때까지 **j = pi[j-1]를 반복**한다.
  + 반복 결과 j = pi[2-1] = 1 이 되었을 때 **문자열[i]와 문자열[j]가 같으므로 반복이 종료**된다.

![image](https://user-images.githubusercontent.com/43658658/117931130-c71ce700-b339-11eb-87a3-0a9d296677be.png)

+ [Step 7] 문자열[i]와 문자열[j]를 비교한다.
  + **두 문자가 같기** 때문에 j를 +1한 후 pi[i] = j 를 기록한다.
  + pi[5] = 2, j = 2

![image](https://user-images.githubusercontent.com/43658658/117931266-f03d7780-b339-11eb-9ef1-c566ea97005e.png)

+ [Step 8] **i가 문자열을 모두 탐색**했으므로 **반복을 종료**하고, **pi 테이블의 마지막 값**을 구한다.
  + **현재 문자열의 최대 접두부 길이는 2**인 것을 알 수 있다.

![image](https://user-images.githubusercontent.com/43658658/117931588-50341e00-b33a-11eb-915d-d60dda28775a.png)

> <h3>실패 함수 파이썬 구현

``` python
l = int(input()) # 문자열 길이
s = input() # 문자열

# 실패 함수
j = 0  # j는 0에서 출발
pi = [0] * l  # 모든 초기값이 0인 문자열 길이(l)만큼의 부분 일치 테이블 생성
for i in range(1, l):  # i는 1부터 시작해 문자열 길이(l)만큼 증가
    while j > 0 and s[j] != s[i]:  # j == 0 or s[j] == s[i]가 될 때까지 반복
        j = pi[j-1]
    if s[j] == s[i]:  # 두 문자가 같으면 j를 +1한 후 부분 일치 테이블 갱신
        j += 1
        pi[i] = j

print(pi[l-1])  # 현재 문자열의 최대 접두부 길이는 부분 일치 테이블(pi)의 마지막 항(l-1번째)
```

[처음으로](#KMP-알고리즘)

---
[참고]
+ https://carstart.tistory.com/143
+ https://developmentdiary.tistory.com/455

---
