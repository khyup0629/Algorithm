# 문제 풀이 아이디어 : 이진 탐색
# 수열의 수를 처음부터 탐색하면서, 양쪽으로 가장 긴 감소하는 부분 수열의 길이를 구하면 된다.
from bisect import bisect_left

n = int(input())

num = list(map(int, input().split()))

result = []
for i in range(n):
    bitonic_1 = [-num[i]]  # 현재 수를 기준으로 왼쪽 부분의 가장 긴 감소하는 부분 수열
    for j in range(i-1, -1, -1):
        if -num[j] > bitonic_1[-1]:
            bitonic_1.append(-num[j])
        else:
            idx = bisect_left(bitonic_1, -num[j])
            bitonic_1[idx] = -num[j]
    bitonic_2 = [-num[i]]
    for j in range(i+1, n):  # 현재 수를 기준으로 오른쪽 부분의 가장 긴 감소하는 부분 수열
        if -num[j] > bitonic_2[-1]:
            bitonic_2.append(-num[j])
        else:
            idx = bisect_left(bitonic_2, -num[j])
            bitonic_2[idx] = -num[j]
    result.append(len(bitonic_1) + len(bitonic_2) - 1)

print(max(result))

# 문제 : https://www.acmicpc.net/problem/11054
