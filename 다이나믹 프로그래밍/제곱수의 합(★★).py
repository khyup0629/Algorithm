# 이중 for 문이지만, 두 번째 for 문이 sqrt(N)이므로
# 총 시간 복잡도는 O(N*N^0.5)인 약 31,600,000번이 되고
# 2초를 넘지 않는다.
from math import *
n = int(input())

dp = [i for i in range(n+1)]  # 최대 경우는 1의 제곱으로만 이루어진 경우로 한다.

for i in range(1, n+1):
    standard = int(sqrt(i))  # i보다 작거나 같은 최대 제곱수를 찾는다.
    # 41의 경우 5^2 + 4^2 가 가장 최소 개수이다.
    for j in range(1, standard+1):
        if dp[i] > dp[i-j**2] + 1:  # 제곱수의 개수가 가장 최소가 되는 값을 찾는다.
            dp[i] = dp[i-j**2] + 1

print(dp[n])

# 문제 : https://www.acmicpc.net/problem/1699
