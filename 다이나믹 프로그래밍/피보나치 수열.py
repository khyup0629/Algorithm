# 문제 풀이 아이디어
# 1. 문제 그대로 재귀 함수로 풀게 되면 시간 초과가 발생합니다.
# 2. dp 테이블을 이용한 피보나치 수열 점화식으로 풀 수 있습니다.

t = int(input())
for _ in range(t):
    n = int(input())
    dp0 = [0] * (n+1)
    dp1 = [0] * (n+1)
    dp0[0] = 1
    dp1[0] = 0
    # 아래의 조건은 인덱스 에러를 방지하기 위함입니다.
    if n >= 1:  # 1보다 크면 dp[1] 값 초기화
        dp0[1] = 0
        dp1[1] = 1
        if n >= 2:  # 2보다 크면 점화식을 이용
            for i in range(2, n+1):
                dp0[i] = dp0[i-1] + dp0[i-2]
                dp1[i] = dp1[i-1] + dp1[i-2]
    print(dp0[n], dp1[n])

# 문제 : https://www.acmicpc.net/problem/1003
