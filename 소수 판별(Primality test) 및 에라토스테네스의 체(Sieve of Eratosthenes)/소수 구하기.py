# m의 범위가 1 이상인 것에 유의해야 합니다.
import math
m, n = map(int, input().split())

primeNumber = [True] * (n + 1)
primeNumber[1] = False
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i * j <= n:
        primeNumber[i * j] = False
        j += 1

for p in range(m, n+1):
    if primeNumber[p]:
        print(p)

# 문제 : https://www.acmicpc.net/problem/1929
