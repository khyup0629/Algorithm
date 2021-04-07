import sys

# input() 대신 sys.stdin.readline()이 컴파일 더 빠름
t = int(sys.stdin.readline())
d = []
for i in range(t):
    n = int(sys.stdin.readline())

    score = []
    for j in range(n):
        x, y = map(int, sys.stdin.readline().split(' '))
        score.append([x, y])
    score.sort()
# 오름차순으로 정렬하면 2번째 성적만 비교해서 기준 순위를 갱신하면서
# 높은 순위만 찾으면 됨
# 기존에 생각한 방법도 틀리진 않았으나 시간 초과
    rank_min = score[0][1]
    people_max = 1

    for j in range(1, n):
        if rank_min > score[j][1]:
            people_max += 1
            rank_min = score[j][1]

    d.append(people_max)

for i in d:
    print(i)
'''
(시간초과)

# for문 2번의 반복을 해결할 더 나은 최적의 방법이 필요

import sys

n = int(sys.stdin.readline())
d = []
for i in range(n):
    nc = int(input())

    people_max = nc
    score = []
    for j in range(nc):
        x, y = map(int, sys.stdin.readline().split(' '))
        score.append([x, y])
    score.sort()
    score.reverse()

    for j in range(nc-1):
        for k in range(j, nc-1):
            if score[j][1] > score[k+1][1]:
                people_max -= 1
                break
    d.append(people_max)

for i in d:
    print(i)
'''