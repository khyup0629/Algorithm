# 문제 풀이 아이디어
# 어떤 수까지 도달하면 그 수부터 처음 수까지 거꾸로 탐색하며
# 그 수들보다 작은 수들에 저장된 dp 테이블 값이
# 제일 큰 값에 자신의 수를 더한 값을 dp 테이블에 넣는다.
import sys
input = sys.stdin.readline
n = int(input())

num = list(map(int, input().split()))

dp = [0] * n
dp[0] = num[0]
for i in range(1, n):
    _max = 0
    for j in range(i-1, -1, -1):
        if num[j] < num[i]:
            _max = max(_max, dp[j])
    dp[i] = num[i] + _max

print(max(dp))

# 문제 : https://www.acmicpc.net/problem/11055
