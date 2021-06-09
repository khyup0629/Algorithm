# for s1 { for s2 } 로 탐색하고, s1을 행, s2를 열로 한 2차원 dp 테이블을 만들어서
# 점화식을 이용한다.
# dp[i][j]는 s1의 i번째까지, s2의 j번째까지의 문자열의 LCS를 의미한다.
s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

dp = [[0] * (n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

# 문제 : https://www.acmicpc.net/problem/9251

"""
  ' C A P C A K
' 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1
C 0 1 1 1 2 2 2
A 0 1 2 2 2 3 3
Y 0 1 2 2 2 3 3
K 0 1 2 2 2 3 4
P 0 1 2 2 2 3 4
dp[i][j]는 s1의 i번째까지, s2의 j번째까지의 문자열의 LCS
"""
