# 원소 하나씩 다 더하면 시간 초과
# 1. 행 별로 누적 합을 진행
# 2. 행을 하나씩 탐색하며 행 별 j ~ y까지 부분 합을 모두 더한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    dp_i = [0] * (m + 1)
    num = [0] + list(map(int, input().split()))
    for i in range(1, m+1):
        dp_i[i] = dp_i[i-1] + num[i]
    array.append(dp_i)

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1; x -= 1  # 인덱스를 맞춰주기 위해
    hap = 0
    for index in range(i, x+1):  # 행 하나씩 탐색
        hap += array[index][y] - array[index][j-1]  # j ~ y까지 부분 합을 모두 더한다.
    print(hap)

# 문제 : https://www.acmicpc.net/problem/2167
