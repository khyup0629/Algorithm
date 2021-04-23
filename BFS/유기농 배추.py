# PyPy3 제출

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0  # 방문 완료
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0  # 방문 완료
                    q.append((nx, ny))


for _ in range(t):
    # 가로 길이, 세로 길이, 위치의 개수
    m, n, k = map(int, input().split())
    # 배추가 놓여진 곳 : 1, 없는 곳 : 0
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)  # 근처의 1을 0으로 만드는 작업
                result += 1  # 그룹의 개수

    print(result)
