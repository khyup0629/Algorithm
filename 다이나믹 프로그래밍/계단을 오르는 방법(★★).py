# 계단 수 numStairs의 범위는 1 <= numStairs <= 70
# 계단은 1, 2, 3칸씩 오를 수 있을 때 계단 수에 대한 계단을 오르는 방법은 모두 몇 개가 있는가.
# 문제 풀이 아이디어
# 1. 1부터 dp 테이블을 채워나갑니다.
# 2. 인덱스 1, 2, 3의 경우 초깃값을 넣어줍니다.
# 3. 인덱스 4부터 맨처음에 계단을 1칸 올랐을 때, 2칸 올랐을 때, 3칸 올랐을 때의 경우로 나눠서 생각해봅시다.
# - 1칸 올랐을 때 : 남은 칸 수가 3칸이고 dp[3]의 값이 계단을 오르는 방법의 수입니다.
# - 2칸 올랐을 때 : 남은 칸 수가 2칸이고 dp[2]의 값이 계단을 오르는 방법의 수입니다.
# - 3칸 올랐을 때 : 남은 칸 수가 1칸이고 dp[1]의 값이 계단을 오르는 방법의 수입니다.
# 3가지의 경우를 모두 더한 값이 바로 계단 수 4칸의 계단 오르는 방법의 수가 되고, dp[4]의 값이 됩니다.
# 4. 마찬가지로 5부터 위와 같은 방법(점화식 : dp[i] = dp[i-1] + dp[i-2] + dp[i-3])으로 차근차근 구해나갈 수 있습니다.

def solution(numStairs):
    dp = [0] * (numStairs + 1)
    if numStairs >= 1:
        dp[1] = 1
        if numStairs >= 2:
            dp[2] = 2
            if numStairs >= 3:
                dp[3] = 4
                if numStairs >= 4:
                    for i in range(4, numStairs+1):
                        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[numStairs]


numStairs = 70
print(solution(numStairs))
