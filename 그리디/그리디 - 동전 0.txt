import sys

N, K = map(int, sys.stdin.readline().split(' '))

A = []
for i in range(N):
    x = int(sys.stdin.readline())
    A.append(x)

count = [int(0) for i in range(N)]

A.reverse()
# 기준 단위마다 한 번씩 차감하는 방법은 시간 초과
# 큰 단위부터 나머지로 구하는 방법이 시간 단축
for i in range(N):
    if K >= A[i]:
        count[i] = K // A[i]
        K = K % A[i]

result = 0
for i in count:
    result += i

print(result)
