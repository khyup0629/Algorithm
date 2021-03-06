# DP의 점화식을 찾지 못해서 아이디어를 참고해야 했던 문제.
# 1. 목표치인 k원까지 DP테이블을 만든다.
# 2. 동전을 하나씩 탐색하며, 그 동전을 추가했을 때 DP 테이블을 갱신한다.
# 3. 동전의 가치인 i원 밑의 가격은 변경되지 않으므로 위만 고려한다. 1씩 증가시키면서 DP테이블을 갱신한다.
# 4. 현재 j원의 dp테이블 값은 i번째 전에 경우에서 i원의 동전이 추가된 경우를 더해준 것과 같다.
# dp[j] += dp[j-i]
n, k = map(int, input().split())

coin = []
for _ in range(n):
    num = int(input())
    coin.append(num)

dp = [0] * (k + 1)
dp[0] = 1
for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])

"""
[1]원을 썼을 때
합이 1원일 때 변경 -> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
합이 2원일 때 변경 -> [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
합이 3원일 때 변경 -> [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
합이 4원일 때 변경 -> [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
합이 5원일 때 변경 -> [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
합이 6원일 때 변경 -> [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
합이 7원일 때 변경 -> [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
합이 8원일 때 변경 -> [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
합이 9원일 때 변경 -> [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
합이 10원일 때 변경 -> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 2]원을 썼을 때
합이 2원일 때 변경 -> [1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
합이 3원일 때 변경 -> [1, 2, 2, 1, 1, 1, 1, 1, 1, 1]
합이 4원일 때 변경 -> [1, 2, 2, 3, 1, 1, 1, 1, 1, 1]
합이 5원일 때 변경 -> [1, 2, 2, 3, 3, 1, 1, 1, 1, 1]
합이 6원일 때 변경 -> [1, 2, 2, 3, 3, 4, 1, 1, 1, 1]
합이 7원일 때 변경 -> [1, 2, 2, 3, 3, 4, 4, 1, 1, 1]
합이 8원일 때 변경 -> [1, 2, 2, 3, 3, 4, 4, 5, 1, 1]
합이 9원일 때 변경 -> [1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
합이 10원일 때 변경 -> [1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
[1, 2, 5]원을 썼을 때
합이 5원일 때 변경 -> [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
합이 6원일 때 변경 -> [1, 2, 2, 3, 4, 5, 4, 5, 5, 6]
합이 7원일 때 변경 -> [1, 2, 2, 3, 4, 5, 6, 5, 5, 6]
합이 8원일 때 변경 -> [1, 2, 2, 3, 4, 5, 6, 7, 5, 6]
합이 9원일 때 변경 -> [1, 2, 2, 3, 4, 5, 6, 7, 8, 6]
합이 10원일 때 변경 -> [1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
"""

# 문제 : https://www.acmicpc.net/problem/2293
