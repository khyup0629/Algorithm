# 피타고라스 공식을 이용해 각 별들 사이의 거리(비용)을 모두 구해준 뒤
# 그래프를 정리한 상태에서 최소 신장 트리를 이용했다.
# '행성 터널' 문제를 푼 직후에 풀어서 '행성 터널'의 최소 간선만 구하는 방법을 이용할 수 있을까 했는데
# 각 x, y 좌표를 따로 정렬해도 비용을 구할 때는 x, y가 서로 연관되어 있어서인지 답이 틀렸다.
# 따라서, 입력값의 범위도 넓지 않은 만큼 모든 간선의 비용을 구해서 문제를 해결하였다.

import math
n = int(input())

parent = [i for i in range(n)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a


cor = []
for i in range(n):
    x, y = map(float, input().split())
    cor.append((x, y))

graph = []
for i in range(n-1):
    for j in range(i+1, n):
        graph.append((math.sqrt((cor[j][0]-cor[i][0])**2+(cor[j][1]-cor[i][1])**2), i, j))

graph.sort()

result = 0
for cost, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(format(result, '.2f'))
