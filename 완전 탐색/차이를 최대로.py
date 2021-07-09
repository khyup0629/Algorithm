# 입력값의 범위가 8이하이므로 순열(permutations)을 임포트해서 사용 가능하다.
from itertools import permutations
n = int(input())

arr = list(map(int, input().split()))

permu = list(permutations(arr, n))

_max = 0
for k in range(len(permu)):
    result = 0
    for i in range(n-1):
        result += abs(permu[k][i]-permu[k][i+1])
    _max = max(_max, result)

print(_max)

# 문제 : https://www.acmicpc.net/problem/10819
