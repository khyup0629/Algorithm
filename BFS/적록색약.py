# 적록색약일 경우 R과 G를 같은 경우로 조건문을 작성해서 BFS 를 수행하면 된다.

from collections import deque
n = int(input())

graph = [input() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color, stand):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if stand == 0:  # 적록색약 X인 경우
                    if not visited[nx][ny] and graph[nx][ny] == color:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                else:  # 적록색약인 경우
                    if color == 'R' or color == 'G':
                        if not visited[nx][ny] and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                    else:
                        if not visited[nx][ny] and graph[nx][ny] == color:
                            visited[nx][ny] = 1
                            q.append((nx, ny))


result_1, result_2 = 0, 0

visited = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            bfs(x, y, graph[x][y], 0)
            result_1 += 1  # 적록색약 X

visited = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            bfs(x, y, graph[x][y], 1)
            result_2 += 1  # 적록색약 O

print(result_1, result_2)

# 문제 : https://www.acmicpc.net/problem/10026
