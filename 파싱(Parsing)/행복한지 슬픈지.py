s = input()

# :-) : happy, :-( : sad
happy, sad = 0, 0
for i in range(len(s)):
    if s[i] == '-':
        try:  # '-' 기준으로 앞뒤로 ':'와 ')','('를 체크해서 happy 와 sad 의 수를 체크한다.
            if s[i-1] == ':' and s[i+1] == ')':
                happy += 1
            elif s[i-1] == ':' and s[i+1] == '(':
                sad += 1
        except:  # '-'가 문자열의 맨 앞 또는 맨 뒤쪽에 위치할 때 인덱스 에러가 뜬다.
            continue

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')

# 문제 : https://www.acmicpc.net/problem/10769
