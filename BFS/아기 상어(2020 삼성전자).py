from collections import deque

n = int(input())

graph = []
for _ in range(n):
    array = list(map(int, input().split()))
    graph.append(array)

visited = [[False] * n for _ in range(n)]
cost = [[int(1e9)] * n for _ in range(n)]
shark_size = 2
tim, cnt = 0, 0


def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    cost[start_x][start_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                cost[nx][ny] = min(cost[nx][ny], cost[x][y] + 1)
                q.append((nx, ny))


# 상어 초기 위치 찾기
now_x, now_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            now_x, now_y = i, j
        if graph[i][j] > shark_size:
            visited[i][j] = True

while True:
    bfs(now_x, now_y)
    eat = []
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < shark_size:
                eat.append((cost[i][j], i, j))

    if not eat:
        break

    eat.sort(key=lambda x:(x[0], x[1], x[2]))

    a, now_x, now_y = eat.pop(0)
    if a >= int(1e9):  # a가 무한대란 뜻은 가는 길이 막혔다는 뜻임.
        break
    graph[now_x][now_y] = 0
    tim += a
    cnt += 1

    if cnt == shark_size:
        cnt = 0
        shark_size += 1

    visited = [[False] * n for _ in range(n)]
    cost = [[int(1e9)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > shark_size:
                visited[i][j] = True

print(tim)

# 문제 : https://www.acmicpc.net/problem/16236

"""
예제 입력 7
4
2 4 1 1
0 4 0 0
0 4 9 0
0 4 0 0
예제 출력 7
3
"""