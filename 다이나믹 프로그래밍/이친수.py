n = int(input())

dp = [0] * (90 + 1)

dp[1] = 1
dp[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# 문제 : https://www.acmicpc.net/problem/2193
