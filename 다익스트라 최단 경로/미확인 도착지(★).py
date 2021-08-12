# 다익스트라를 한 번만 쓰면서 더욱 간결해지고 속도 또한 개선된 코드
# 문제 풀이 아이디어
# 1. 간선의 가중치를 둡니다. 간선의 비용을 2배로 두어 짝수로 맞춰줍니다.
# 2. 반드시 지나야 할 간선의 가중치는 2배 -1로 맞춰줍니다.
# 3. 다익스트라로 각 노드의 최단 거리를 구했을 때 노드의 최단 거리가 홀수라면 `반드시 지나야 하는 간선`을 지난 것입니다.
# 마지막 출력에서 join을 쓰기 위해 문자열로 바꾼 후 정렬을 하면 숫자가 커졌을 때 이상하게 정렬됩니다.
# 이 부분을 간과한 채 반례를 찾느라 풀이 시간이 늦어졌습니다. 아이디어는 진작에 맞았습니다.

import heapq
T = int(input())

for _ in range(T):
    # input
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]  # 그래프
    for _ in range(m):
        a, b, d = map(int, input().split())
        # g-h 경로일 경우 간선 비용의 가중치를 2배 -1
        if (a == g and b == h) or (a == h and b == g):
            graph[a].append((b, d * 2 - 1))
            graph[b].append((a, d * 2 - 1))
        else:  # g-h 경로가 아닐 경우 간선 비용의 가중치 2배
            graph[a].append((b, d * 2))
            graph[b].append((a, d * 2))

    dist = [int(1e9)] * (n + 1)


    def dijkstra(s):
        q = []
        heapq.heappush(q, (0, s))
        dist[s] = 0
        while q:
            distance, now = heapq.heappop(q)
            if distance > dist[now]:
                continue
            for x, cost in graph[now]:
                newCost = distance + cost
                if dist[x] > newCost:
                    dist[x] = newCost
                    heapq.heappush(q, (newCost, x))


    dijkstra(s)
    result = []  # g-h 경로를 지나는 최단 거리 노드들 저장
    for _ in range(t):
        x = int(input())  # 목적지 후보
        if dist[x] % 2 == 1:  # 목적지 후보까지의 최단 거리가 홀수일 경우 g-h 경로를 지난 것입니다.
            result.append(x)
    # join을 쓰기 위해 문자로 만들어서 정렬할 경우 숫자가 커질 때 이상하게 정렬될 수 있습니다.
    # 따라서, 정렬이 포함되었을 때는 join을 쓰려고 하지말고 아래와 같은 방식으로 출력하도록 합시다.
    result.sort()
    for r in result:
        print(r, end=' ')
    print()

# 다른 풀이 방법
# 1. 각 노드까지의 최단 거리를 다익스트라로 구합니다.
# 2. 목적지 후보 노드들로부터 백트래킹을 통해 거슬러 내려옵니다.
# 3. 내려오면서 g-h 경로를 지날 경우 해당 목적지 후보 노드를 가능한 목적지 노드로 취급합니다.
# (최단 거리의 경로가 여러개가 있어도 아래의 백트래킹 알고리즘을 통해 거슬러 내려오면
# g-h 경로를 반드시 지나게 됩니다)
from collections import deque
import heapq
T = int(input())

for _ in range(T):
    # input
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]  # 그래프
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dist = [int(1e9)] * (n + 1)


    def dijkstra(s):
        q = []
        heapq.heappush(q, (0, s))
        dist[s] = 0
        while q:
            distance, now = heapq.heappop(q)
            if distance > dist[now]:
                continue
            for x, cost in graph[now]:
                newCost = dist[now] + cost
                if dist[x] > newCost:
                    dist[x] = newCost
                    heapq.heappush(q, (newCost, x))

    
    # 백트래킹 중요 고려 사항
    # 1. 현재 위치 비용 - 간선의 비용 = 다음 위치 비용 일 때 다음 위치 노드를 q에 추가합니다.
    # 2. 중복으로 q에 추가되는 것을 막기 위해 visited를 이용합니다.
    def backTracking(destination):  # 백트래킹
        visited = [False] * (n + 1)
        visited[destination] = True
        q = deque()
        q.append(destination)
        while q:
            now = q.popleft()
            for x, cost in graph[now]:
                if dist[now] - cost == dist[x]:
                    # 서로 다른 노드에서 같은 x를 향해 올 수 있으므로 if not visited[x] 밖에 있어야합니다.
                    if (now == g and x == h) or (now == h and x == g):
                        result.append(destination)
                    if not visited[x]:  # q에 중복으로 추가되는 것을 막기 위한 코드
                        visited[x] = True
                        q.append(x)


    dijkstra(s)
    result = []
    for _ in range(t):
        x = int(input())  # 목적지 후보
        backTracking(x)
    result.sort()
    for r in result:
        print(r, end=' ')
    print()
    
# 문제 : https://www.acmicpc.net/problem/9370
