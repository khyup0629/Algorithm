# float(n) * (10 ** (n1 + n2)) = 899.99999가 나오는 이유를 모르겠다.
# 소수점으로 된 문자열을 float 로 실수로 바꿔주었을 경우 계산이 원활히 되지 않는 문제가 있다.
# 문제 풀이 아이디어:
# 1. 분자 : 전체 유효숫자 - 비순환숫자
# 2. 분모 : 순환숫자의 개수만큼 9 + '소숫점 이하' 비순환숫자의 개수만큼 0
# 3. 유클리드 호제법을 이용해 시간 복잡도를 줄여서 최대 공약수를 찾은 다음 분자와 분모에 나눠서 기약분수를 구한다.

# ex) 1.0(123)
# 분자 : 10123(1.0123) - 10(1.0)
# 분모 : 999(123) + 0(0) = 9990
# ex) 0.6(142857)
# 분자 : 6142857 - 6
# 분모 : 9999990
# ex) 0.00(900)
# 분자 : 900 - 00
# 분모 : 99900
def gcd(a, b):  # 유클리드 호제법
    while b != 0:
        n = a % b
        a = b
        b = n
    return a


t = int(input())
for _ in range(t):
    num = ''  # 유한 소수
    inf = ''  # 순환 소수
    a = input()
    idx = len(a)
    for i in range(2, len(a)):  # 유한 소수
        if a[i] == '(':
            idx = i
            break
        num += a[i]
    for i in range(idx+1, len(a)-1):  # 순환 소수
        inf += a[i]
    # 분자와 분모로 나누기
    if inf == '':  # 순환 소수가 없다면,
        son = int(num)
        parent = 10 ** len(num)
    else:  # 순환 소수가 있다면,
        n1 = len(num)
        n2 = len(inf)
        if num == '':
            num = '0'
        son = int(num+inf) - int(num)
        parent = int('9' * n2 + '0' * n1)

    # 기약분수 구하기
    g = gcd(parent, son)
    son //= g
    parent //= g

    print(str(son)+'/'+str(parent))

# 문제 : https://www.acmicpc.net/problem/5376
