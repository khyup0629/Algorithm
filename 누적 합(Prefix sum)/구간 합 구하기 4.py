# i ~ j까지 일일이 다 더하면 시간 초과 발생
# 누적 합 이용
import sys
input = sys.stdin.readline  # 시간 초과 방지(입력 빠르게)

n, m = map(int, input().split())
num = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + num[i]

for _ in range(m):
    i, j = map(int, input().split())
    hap = dp[j] - dp[i-1]
    print(hap)

# 문제 : https://www.acmicpc.net/problem/11659
