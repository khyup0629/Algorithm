from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    graph[nx][ny] = cnt


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            graph[i][j] = cnt
            bfs(i, j)

visitIsland = [False] * (cnt + 1)  # 섬이 연결되었는지 여부
edge = []
for i in range(n):
    for j in range(m):
        if graph[i][j] >= 1:
            for pos in range(4):
                ni, nj = i + dx[pos], j + dy[pos]
                while 0 <= ni < n and 0 <= nj < m:
                    if graph[ni][nj] >= 1:
                        dist = abs(ni - i) + abs(nj - j)
                        if dist >= 3 and graph[ni][nj] != graph[i][j]:
                            edge.append((dist-1, graph[i][j], graph[ni][nj]))
                            visitIsland[graph[i][j]] = True
                            visitIsland[graph[ni][nj]] = True
                        break
                    ni += dx[pos]
                    nj += dy[pos]

edge = list(set(edge))
edge.sort()
parent = [i for i in range(cnt+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


result = 0
for dist, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        result += dist

allConnection = True
for v in visitIsland[1:]:
    if not v:
        allConnection = False

if result == 0 or not allConnection:
    print(-1)
else:
    print(result)
print(graph)
print(edge)
print(visitIsland)

# 문제 : https://www.acmicpc.net/problem/17472
