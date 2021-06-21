# 누적합을 이용한다.
# 1. 열을 기준으로 누적합 테이블을 구한다.
# 2. 가로로 각 행 당 요구되는 구간 합을 구한다.
# 3. 가로로 구한 구간 합을 모두 더한다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

# 누적 합 테이블 => i : 0 ~ n, j : 0 ~ n+1
dp = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + graph[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for i in range(x1-1, x2):
        result += (dp[i][y2] - dp[i][y1-1])
    print(result)

# 문제 : https://www.acmicpc.net/problem/11660
