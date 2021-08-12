# PyPy3 제출
# 그냥 계산시간이 조금이라도 많이 걸릴 것 같으면 PyPy로 제출하자.
# 다익스트라 알고리즘은 힙 자료구조를 이용해 우선순위 큐를 이용합니다.

import heapq
# 노드의 개수, 간선의 개수
V, E = map(int, input().split())
# 최단거리 시작 노드
start = int(input())
# 인덱스를 시작노드로 하고, (도착 노드, 가중치) 형식으로 저장
graph = [[] for _ in range(V+1)]
for _ in range(E):
    # u : 시작 노드, v : 도착 노드, w : 가중치
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
# 최단 거리를 저장하는 노드 생성
INF = int(1e9)
dist = [INF] * (V + 1)


def dijkstra(start):
    q = []
    # 시작 노드에 대한 초기값 정리
    # 힙 자료구조에 [밝혀진 최단거리, 시작 노드] 형식으로 넣는다.
    heapq.heappush(q, [0, start])
    dist[start] = 0
    # 힙 자료구조에 의해 w가 가장 낮은 값이 저장됨
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:  # 방문 완료의 역할
            continue
        for i in graph[now]:
            # i는 [v, w]의 형태의 리스트이다.
            cost = distance + i[1]
            # 노드까지의 알려진 비용이 현재 계산된 노드보다 크면 갱신
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


dijkstra(start)

for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)

# 문제 : https://www.acmicpc.net/problem/1753
