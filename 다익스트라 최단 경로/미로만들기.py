# 벽의 비용을 크게(10000) 주고 벽도 고려한채로 (n, n)까지의 최단거리를 계산하면
# 벽을 어쩔 수 없이 통과해야할 때, 몇 개의 벽을 통과하는지가 (n, n)까지의 최단거리 정보에 담기게 된다.
# (n, n)까지의 최단거리에서 10000을 나눈 몫이 벽을 통과해야하는 갯수이다.
import heapq
n = int(input())

graph = []
for _ in range(n):
    arr = input()
    graph.append(arr)

dist = [[int(1e9)] * n for _ in range(n)]
cost = [[10000] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            cost[i][j] = 1


def dijkstra(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    heapq.heappush(q, (0, x, y))
    dist[x][y] = 0
    while q:
        distance, now_x, now_y = heapq.heappop(q)
        if dist[now_x][now_y] < distance:
            continue
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                n_cost = distance + cost[nx][ny]
                if dist[nx][ny] > n_cost:
                    dist[nx][ny] = n_cost
                    heapq.heappush(q, (n_cost, nx, ny))


dijkstra(0, 0)

print(dist[n-1][n-1] // 10000)

# 문제 : https://www.acmicpc.net/problem/2665
