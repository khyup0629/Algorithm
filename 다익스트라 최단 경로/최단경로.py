# PyPy3 제출
# 그냥 계산시간이 조금이라도 많이 걸릴 것 같으면 PyPy로 제출하자.

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
        if dist[now] < distance:
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

"""
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF 를 출력하면 된다.

예제 입력 1 
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
예제 출력 1 
0
2
3
7
INF
"""