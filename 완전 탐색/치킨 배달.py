from itertools import combinations
n, m = map(int, input().split())

graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

combi = list(combinations(chicken, m))
lst = []
for i in combi:
    result = 0
    for h1, h2 in house:
        _min = int(1e9)
        for c1, c2 in i:
            if abs(c1-h1) + abs(c2-h2) < _min:
                _min = abs(c1-h1) + abs(c2-h2)
        result += _min
    lst.append(result)

print(min(lst))

# 문제 : https://www.acmicpc.net/problem/15686
