# 각 경로의 비용이 일정한 문제로 BFS 사용 가능
from collections import deque


def bfs(x, y):
    # deque : 양방향에서 데이터를 처리할 수 있는 queue 형 자료구조
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]


N, M = map(int, input().split(' '))

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
