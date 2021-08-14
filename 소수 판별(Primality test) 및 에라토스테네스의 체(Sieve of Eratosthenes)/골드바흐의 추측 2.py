# 문제 풀이 아이디어
# 1. 문제의 조건이 4~1000000 범위의 짝수이므로 계산 시간을 줄이기 위해
# 소수의 집합을 구할 때 1000000까지 한 번만 계산하도록 했습니다.
# 2. b-a의 차이가 가장 큰 값을 구해야하기 때문에 for문을 하나만 사용해서
# 범위를 2~n까지 탐색하도록 합니다. 그럼 최초로 발견되는 a, b의 값이 가장 차이가 큰 두 수가 됩니다.
import math
# 소수 구하기(~1,000,000)
primeNumber = [True] * (1000000 + 1)
primeNumber[1] = False
for i in range(2, int(math.sqrt(1000000))+1):
    j = 2
    while i * j <= 1000000:
        primeNumber[i*j] = False
        j += 1

while True:
    n = int(input())
    if n == 0:
        break

    a, b = 0, 0
    for i in range(2, n+1):
        if primeNumber[i] and primeNumber[n-i] and i % 2 == 1 and (n-i) % 2 == 1:
            a, b = i, n-i
            break

    if a == 0 and b == 0:  # a, b가 초기값을 가진다는 것은 두 수가 소수이자 홀수일 수 없다는 것입니다.
        print("Goldbach's conjecture is wrong.")
    else:
        print(str(n) + " = " + str(a) + " + " + str(b))

# 문제 : https://www.acmicpc.net/problem/6588
