# 에라토스테네스의 체 알고리즘을 활용해 푼다.

import math

while True:
    n = int(input())

    if n == 0:
        break

    prime_num = [True] * (2 * n + 1)
    for i in range(2, int(math.sqrt(2*n))+1):
        j = 2
        while i*j <= 2 * n:
            prime_num[i*j] = False
            j += 1

    cnt = 0
    for i in range(2, len(prime_num)):
        if prime_num[i] and (n < i <= 2 * n):
            cnt += 1

    print(cnt)

# 문제 : https://www.acmicpc.net/problem/4948
