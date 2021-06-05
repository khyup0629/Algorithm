from collections import deque
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

graph = []
for _ in range(h):
    arr = []
    for _ in range(m):
        a = list(map(int, input().split()))
        arr.append(a)
    graph.append(arr)

# 앞, 뒤, 좌, 우, 상, 하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
days = 0

q = deque()
temp = []
for z in range(h):
    for x in range(m):
        for y in range(n):
            if graph[z][x][y] == 1:
                temp.append((z, x, y))
q.append(temp)

while q:
    t = q.popleft()
    temp = []
    for z, x, y in t:
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    temp.append((nz, nx, ny))
    if not temp:
        break
    q.append(temp)
    days += 1

result = True
for z in range(h):
    for x in range(m):
        for y in range(n):
            if graph[z][x][y] == 0:
                result = False

if result:
    print(days)
else:
    print(-1)

# 문제 : https://www.acmicpc.net/problem/7569
