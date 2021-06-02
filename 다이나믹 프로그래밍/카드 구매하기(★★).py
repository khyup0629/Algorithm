n = int(input())
num = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = num[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + num[j]:
            dp[i] = dp[i-j] + num[j]

print(dp[n])

# 문제 : https://www.acmicpc.net/problem/11052
