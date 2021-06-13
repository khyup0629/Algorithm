# 이중 for 문이지만, 두 번째 for 문이 sqrt(N)이므로
# 총 시간 복잡도는 O(N*N^0.5)인 약 31,600,000번이 되고
# 2초를 넘지 않는다.
from math import *
n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    standard = int(sqrt(i))
    for j in range(1, standard+1):
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1

print(dp[n])

# 문제 : https://www.acmicpc.net/problem/1699
