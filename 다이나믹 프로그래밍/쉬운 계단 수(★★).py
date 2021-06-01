# 그래프를 그려보면 작은 단위로 쪼갤 수 있기 때문에 DP인 것을 알았지만
# 점화식으로 어떻게 표현할지를 많이 고민했던 문제.
# 1. dp 테이블을 2차원 배열로 나타낸다. 행:각 자리, 열:숫자
# 2. (행, 열)의 원소는 '열'의 숫자부터 시작해 '행'번째 자리 수까지 개수
# 3. 1행의 원소는 전부 1로 채워준다.(초기값)
n = int(input())

dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)

# 문제 : https://www.acmicpc.net/problem/10844
