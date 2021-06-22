from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)
cost = [[0] * m for _ in range(n)]


def bfs(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0:
                    q.append((nx, ny))
                else:
                    cnt += 1
            if i == 3:
                cost[x][y] = cnt
    graph -= cost


i = 0
while True:
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                bfs(i, j)
                result += 1
    if result > 1:
        print(i)
        break
    i += 1
