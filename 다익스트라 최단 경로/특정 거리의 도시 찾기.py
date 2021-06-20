# 다익스트라 알고리즘을 이용
# 1. 출발 노드부터 각 노드까지의 최단 거리를 구한다.
# 2. 모든 노드를 탐색하면서 최단 거리가 k와 같은 노드를 result에 모은다.
# 3. 만약 result가 비어있다면 -1 출력, 아닐 경우 하나씩 출력한다.
# (이때, result에는 오름차순으로 노드가 들어가 있으므로 그냥 출력하면 된다)
import heapq
import sys
input = sys.stdin.readline
# 도시의 개수, 간선의 개수, 최단 거리, 출발 도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [int(1e9)] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            n_cost = distance + 1
            if dist[i] > n_cost:
                dist[i] = n_cost
                heapq.heappush(q, (n_cost, i))


dijkstra(x)

result = []
for i, cost in enumerate(dist):
    if cost == k:
        result.append(i)

if not result:
    print(-1)
else:
    for i in result:
        print(i)

# 문제 : https://www.acmicpc.net/problem/18352
