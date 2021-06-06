# 문제 풀이 아이디어
# 1. 3차원 dist 배열을 생성한다. [stand][x][y] 형태로 생성한다.
# stand는 벽을 뚫을 수 있는지(1) 없는지(0)의 상태를 나타낸다.
# 즉, dist 배열의 종류를 둘로 나눈다.
# 2. 큐에는 (stand, x, y)의 형태로 자료를 넣는다. 큐는 하나로 굴리되, stand 값에 따라 나눠서 진행되도록 한다.
# 3. 처음에는 벽을 뚫을 수 있는 상태(stand=1)로 시작한다. 이 상태에서 '1'을 만나면
# 벽을 뚫을 수 없는 상태(stand=0)의 dist 배열의 값을 갱신한다.
# 4. stand 가 0이든 1이든 상관없이 도착점에 먼저 도착할 때의 dist[stand][x][y]의 값이 최단거리 값이 된다.
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    num = list(input())
    graph.append(num)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 1. 3차원 배열을 생성한다. [벽을 뚫을 수 있는 경우][x][y] 형태로 나타낸다.
dist = [[[0] * m for _ in range(n)], [[0] * m for _ in range(n)]]


def bfs():
    q = deque()
    # 2. 큐에는 (stand, x, y)의 형태로 자료를 넣는다. 큐는 하나로 굴리되, stand 값에 따라 나눠서 진행되도록 한다.
    q.append((1, 0, 0))
    # 3. 처음에는 벽을 뚫을 수 있는 상태(stand=1)로 시작한다.
    dist[1][0][0] = 1
    while q:
        stand, now_x, now_y = q.popleft()
        # 4. stand 가 0이든 1이든 상관없이 도착점에 먼저 도착할 때의 dist[stand][x][y]의 값이 최단거리 값이 된다.
        if now_x == n-1 and now_y == m-1:
            return dist[stand][now_x][now_y]
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 뚫을 수 있는 상태에서 1을 만났을 때 벽을 뚫을 수 없는 상태의 dist 배열의 값을 갱신한다.
                if graph[nx][ny] == '1' and stand == 1:
                    dist[0][nx][ny] = dist[1][now_x][now_y] + 1
                    q.append((0, nx, ny))
                # stand 가 0이든 1이든 상관없이 아직 방문하지 않은 dist 요소를 방문했는데 빈 방이라면,
                # 벽을 뚫을 수 없는 상태의 dist 배열의 값 갱신.
                elif graph[nx][ny] == '0' and dist[stand][nx][ny] == 0:
                    dist[stand][nx][ny] = dist[stand][now_x][now_y] + 1
                    q.append((stand, nx, ny))
    return -1


print(bfs())

# 문제 : https://www.acmicpc.net/problem/2206


# 시간 초과
from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    num = list(input())
    graph.append(num)

cost = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == '1':
            cost.append((x, y))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '1':
                n_cost = dist[now_x][now_y] + 1
                if dist[nx][ny] > n_cost:
                    dist[nx][ny] = n_cost
                    q.append((nx, ny))


result = []
for x, y in cost:
    graph[x][y] = '0'
    dist = [[int(1e9)] * m for _ in range(n)]
    bfs(0, 0)
    graph[x][y] = '1'
    result.append(dist[n-1][m-1])

_min = min(result)
if _min == int(1e9):
    print(-1)
else:
    print(_min)
