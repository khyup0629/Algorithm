# 우선순위 큐에 (거리, 노드 번호) 형식으로 값을 저장하는 원리
# 방문 여부 리스트를 생성할 필요 없다. 우선순위로 뽑혀나온 노드까지의 거리가
# 기존 노드까지의 최단 거리보다 크다면 방문된 노드라고 할 수 있기 때문이다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a 인덱스에 [도착 노드, 거리] 저장
    graph[a].append([b, c])


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정, 큐에 삽입
    heapq.heappush(q, [0, start])
    dist[start] = 0
    # while 문 : 노드의 개수 V번 반복 계산(우선순위 큐, 힙), for 문 : 간선의 개수 E번 반복 계산
    # 시간 복잡도 O(ElogV), logV : 우선순위 큐의 시간 복잡도
    while q:  # q가 비면 반복 종료.
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        distance, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 우선순위로 뽑혀나온 노드까지의 거리가
        # 기존 노드까지의 최단 거리보다 크다면 방문된 노드라고 할 수 있다.
        if dist[now] < distance:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = distance + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, [dist[i[0]], i[0]])

dijkstra(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
