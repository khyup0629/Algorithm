# DP로도 풀 수 있고, 시간을 단축시키려면 이진 탐색으로도 풀 수 있다.
# 수열의 각 원소에 -를 붙여서 가장 긴 증가하는 부분 수열 문제로 풀면 된다.
from bisect import bisect_left
n = int(input())

A = list(map(int, input().split()))

num = [-A[0]]
for i in range(1, n):
    if num[-1] < -A[i]:
        num.append(-A[i])
    else:
        idx = bisect_left(num, -A[i])
        num[idx] = -A[i]

print(len(num))

# 문제 : https://www.acmicpc.net/problem/11722
