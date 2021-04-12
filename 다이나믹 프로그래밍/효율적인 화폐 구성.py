n, m = map(int, input().split(' '))

unit = []
for i in range(n):
    unit.append(int(input()))

# DP 테이블 초기화, 가능하지 않은 경우에 대해 INF 값
d = [10001] * (m + 1)
# Dynamic Programming, Bottom up
d[0] = 0
for i in range(1, m+1):
    for j in range(n):
        if i - unit[j] >= 0:
            d[i] = min(d[i], d[i - unit[j]] + 1)

if d[m] >= 10001:
    print(-1)
else:
    print(d[m])


"""
단위를 하나씩 고려하면서 최소를 구하는 방법도 있음
for i in range(n):
    for j in range(unit[i], m+1):
        if d[j-unit[i]] != 10001:
            d[j] = min(d[j], d[j-unit[i]] + 1)
"""
"""
입력 조건
- 첫째 줄에 N, M이 주어진다.(1 <= N <= 100, 1 <= M <= 10,000)
- 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건
- 첫째 줄에 최소 화폐 개수를 출력한다.
- 불가능할 때는 -1을 출력한다.

입력 예시1
2 15
2
3

출력 예시1
5

입력 예시2
3 4
3
5
7

출력 예시2
-1
"""