# 문제 풀이 아이디어
# 1. 조합으로 볼 수 있다. 옷의 종류별(b)로 옷(a)을 분류한다.
# 2. (각 옷의 종류별 갯수 + 1)을 모두 곱한 값에 -1을 해준다.
# 옷의 종류별을 안 입는 경우가 존재하는 것을 (각 옷의 종류별 갯수 + 1)로 표현
# 종류별로 옷을 모두 입지 않는 경우는 존재하지 않으므로 위의 값에 -1을 해주는 것이다.
from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    wear = defaultdict(list)

    for _ in range(n):
        a, b = input().split()
        wear[b].append(a)

    result = 1
    for i in wear:
        result *= len(wear[i]) + 1

    print(result - 1)

# 문제 : https://www.acmicpc.net/problem/9375
