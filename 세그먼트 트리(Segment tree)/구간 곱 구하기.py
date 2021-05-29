
# 메모리 초과, 누적 합
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

num = [0] + [int(input()) for _ in range(n)]

dp = [1] * (n + 1)
dp[1] = num[1]
for i in range(1, n+1):
    dp[i] = dp[i-1] * num[i]

arr = {}
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
    else:
        result = dp[c] // dp[b-1]
        for i in arr:
            if i <= c:
                result = (result // num[i]) * arr[i]
        print(result % 1000000007)
