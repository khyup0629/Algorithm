# 발상의 전환, 크로아티아 알파벳을 다른 하나의 문자로 바꿔준 후
# 전체 문장의 길이를 출력
sentence = input()
# 주의해야 할 점은 'dz='를 'z=' 앞에 둬야 한다는 것
# 그래야 'dz='를 먼저 고려한다.
alphabet = ['c=', 'c-', 'dz=', 'd-',
            'lj', 'nj', 's=', 'z=']

for word in alphabet:
    sentence = sentence.replace(word, '*')

print(len(sentence))

"""
# 내가 짠 코드
sentence = input()

alphabet = ['c=', 'c-', 'dz=', 'd-',
            'lj', 'nj', 's=', 'z=']

cnt = 1
for i in range(1, len(sentence)):
    cnt += 1
    if sentence[i] == 'j':
        if sentence[i-1] == 'l' or sentence[i-1] == 'n':
            cnt -= 1
            continue
    if sentence[i] == '=':
        if sentence[i-1] == 'c' or sentence[i-1] == 's':
            cnt -= 1
            continue
        if sentence[i-1] == 'z':
            if sentence[i-2] == 'd':
                cnt -= 2
                continue
            cnt -= 1
            continue
    if sentence[i] == '-':
        if sentence[i-1] == 'c' or sentence[i-1] == 'd':
            cnt -= 1
            continue

print(cnt)
"""

"""
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
위 목록에 없는 알파벳은 한 글자씩 센다.

입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

예제 입력 1 
ljes=njak
예제 출력 1 
6
예제 입력 2 
ddz=z=
예제 출력 2 
3
예제 입력 3 
nljj
예제 출력 3 
3
예제 입력 4 
c=c=
예제 출력 4 
2
"""