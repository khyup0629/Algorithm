# 입력값의 범위가 최대 100,000이었기 때문에 시간 복잡도를 O(N^2) 밑으로 해야 했다.
# 반복문을 하나로 돌리는 방법으로 고려.
# 수열의 처음부터 하나씩 탐색하면서 직전 최댓값과 현재까지 더한 값 중 최댓값을 DP 테이블에 넣는다.
# 만약 더한 값이 음수가 된다면 0으로 초기화시킨 후 그 수부터 다시 더한다.

n = int(input())
array = list(map(int, input().split()))

dp = [0] * n  # DP 테이블
# 초기값
dp[0] = array[0]
temp = array[0]
# 수열의 처음부터 하나씩 탐색
for i in range(1, n):
    # 만약 더한 값이 음수가 된다면 0으로 초기화
    if temp < 0:
        temp = 0
    # 직전 최댓값(dp[i-1])과 현재까지 더한 값(temp) 중 최댓값을 DP 테이블에 넣는다.
    temp += array[i]
    dp[i] = max(dp[i-1], temp)

print(max(dp))

"""
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
33
예제 입력 2 
10
2 1 -4 3 4 -4 6 5 -5 1
예제 출력 2 
14
예제 입력 3 
5
-1 -2 -3 -4 -5
예제 출력 3 
-1
"""