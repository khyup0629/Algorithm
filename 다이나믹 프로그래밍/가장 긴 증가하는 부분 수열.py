n = int(input())
data = list(map(int, input().split(' ')))
# DP 테이블
d = [1] * n
# DP 진행, Bottom up
for i in range(1, n):
    for j in range(i):
        if data[j] < data[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))

"""
입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
"""