# 문제 풀이 아이디어
# 1. dp 테이블을 1부터 채워나갑니다.
# 2. 1, 2는 초기값을 두고, 3부터 2가지 경우를 고려합니다.
# - 1 x 2 직사각형이 1개 있는 경우 : 남아있는 칸이 2칸이므로 dp[2]의 값을 더해줍니다.
# - 2 x 1 직사각형이 2개 있는 경우(합치면 2 x 2 정사각형) : 남아있는 칸이 1칸이므로 dp[1]의 값을 더해줍니다.
# 3. 3부터 n까지 차례대로 dp 테이블을 점화식(dp[i] = dp[i-1] + dp[i-2])을 이용해 채워나갑니다.
n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
# 아래에 if문은 인덱스 에러를 방지하기 위한 조건입니다.
if n >= 2:
    dp[2] = 2
    if n >= 3:
        for i in range(3, n+1):  # 과정마다 10007로 나눠줍니다.
            dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])

# 문제 : https://www.acmicpc.net/problem/11726
