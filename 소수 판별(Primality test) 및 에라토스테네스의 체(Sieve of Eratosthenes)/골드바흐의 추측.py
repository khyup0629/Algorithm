# 아래의 코드보다 개선된 아이디어
# 1. for문을 한 번만 쓰고 n//2 ~ n의 범위를 탐색합니다.
# 2. 최초로 for문의 인덱스와 (n-인덱스)의 값이 모두 소수이면
# 인덱스와 (n-인덱스)는 차이가 가장 작은 두 소수가 됩니다.
# (n-인덱스) < (인덱스)
import sys
import math
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())

    primeNumber = [True] * (n + 1)
    primeNumber[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        j = 2
        while i * j <= n:
            primeNumber[i*j] = False
            j += 1

    a, b = 0, 0
    for i in range(n//2, n+1):
        if primeNumber[i] and primeNumber[n-i]:
            a = n - i
            b = i
            break

    print(a, b)

# 문제 풀이 아이디어
# 1. 이중 for문을 통해서 첫 번째 for문은 n//2 ~ n, 두 번째 for문은 n//2 ~ 2의 범위로 탐색합니다.
# 2. 첫 번째와 두 번째 for문의 인덱스를 더했을 때 n과 같아지는 최초의 순간이 차이가 가장 작은 답이 됩니다.
import sys
import math

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())

    primeNumber = [True] * (n + 1)
    primeNumber[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            primeNumber[i * j] = False
            j += 1

    # 이중 for문
    a, b = 0, 0
    changed = False
    for i in range(n // 2, n + 1):
        if primeNumber[i]:
            for j in range(n // 2, 1, -1):
                if primeNumber[j] and i + j == n:
                    a, b = i, j
                    changed = True
                    break
            if changed:
                break

    if a >= b:
        print(b, a)
    else:
        print(a, b)

# 문제 : https://www.acmicpc.net/problem/9020
