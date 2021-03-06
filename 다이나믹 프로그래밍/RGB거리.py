# 금광 문제와 유사한 문제
# i번째 집이 i-1, i+1의 색과 달라야 하므로,
# 행을 기준으로 -1행의 다른 색의 비용과 현재 위치한 집의 비용을 더해서 최소로 구하도록 한다.

N = int(input())

house = []
for i in range(N):
    house.append(list(map(int, input().split(' '))))

# DP 테이블
d = [[0 for j in range(3)] for i in range(N)]
# DP 테이블 초기값
for i in range(3):
    d[0][i] = house[0][i]
# DP 진행, Bottom up
for i in range(1, N):
    d[i][0] = house[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = house[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = house[i][2] + min(d[i-1][0], d[i-1][1])
# DP 테이블의 마지막 줄에서 최소값 찾기
result = d[N-1][0]
for i in d[N-1]:
    result = min(result, i)

print(result)

"""
문제
RGB 거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
"""