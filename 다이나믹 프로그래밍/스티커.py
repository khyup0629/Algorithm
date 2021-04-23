# 연속하는 열에 대한 제한이 없기 때문에
# 현재 열에서 2열 전까지의 값은 앞의 모든 데이터를 포함하고 있다.
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(2):
        data = list(map(int, input().split()))
        data.append(0)
        graph.append(data)
    # DP 테이블 초기화
    dp = [[0] * (n+1) for _ in range(2)]
    # 초기값 설정
    dp[0][0], dp[1][0] = graph[0][0], graph[1][0]
    dp[0][1], dp[1][1] = dp[1][0] + graph[0][1], dp[0][0] + graph[1][1]
    # 2열부터 진행
    for i in range(2, n+1):  # 연속하는 열에 대해서 제한이 없기 때문에 2열 전의 값만 고려
        dp[0][i] = max(max(dp[0][i-2:i-1]), max(dp[1][i-2:i])) + graph[0][i]
        dp[1][i] = max(max(dp[0][i-2:i]), max(dp[1][i-2:i-1])) + graph[1][i]

    print(max(dp[0][n], dp[1][n]))

"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
1
2
50 10
30 50
"""