import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    # 양방향 이동 가능
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())


def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    dist[x] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[0]
            if dist[i[1]] > cost:
                dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


# 경우의 수는 2가지이다.
# 1 - v1 - v2 - n
# 1 - v2 - v1 - n
hap_1 = 0
# 시작점 : 1, 도착점 : v1
dist = [int(1e9)] * (n + 1)
dijkstra(1)
hap_1 += dist[v1]
# 시작점 : v1, 도착점 : v2
dist = [int(1e9)] * (n + 1)
dijkstra(v1)
hap_1 += dist[v2]
# 시작점 : v2, 도착점 : n
dist = [int(1e9)] * (n + 1)
dijkstra(v2)
hap_1 += dist[n]

hap_2 = 0
# 시작점 : 1, 도착점 : v2
dist = [int(1e9)] * (n + 1)
dijkstra(1)
hap_2 += dist[v2]
# 시작점 : v2, 도착점 : v1
dist = [int(1e9)] * (n + 1)
dijkstra(v2)
hap_2 += dist[v1]
# 시작점 : v1, 도착점 : n
dist = [int(1e9)] * (n + 1)
dijkstra(v1)
hap_2 += dist[n]

# 구한 합의 경우의 수가 하나라도 무한대를 넘으면 노드가 연결되어 있지 않다는 뜻.
if hap_1 >= int(1e9) or hap_2 >= int(1e9):
    print(-1)
else:
    print(min(hap_1, hap_2))

# 문제 : https://www.acmicpc.net/problem/1504

"""
예제 입력 2
4 3
1 2 3
2 3 3
1 3 5
2 3
예제 출력 2
-1
"""