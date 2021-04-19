# 코드의 시간복잡도는 O(V^2) 이므로 입력이 5,000개 이하일 경우 적합
# V : 노드의 개수
# 입력 개수가 5,000을 넘어가는 문제는 다른 효율적인 알고리즘을 짜야 한다.

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미, 10억

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 방문 여부 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    # 1번 노드부터 탐색
    for i in range(1, n+1):
        # 기존 최소값보다 작은 값이면서 방문하지 않은 노드이면
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해 방문 완료 및 최단 경로 0
    visited[start] = True
    dist[start] = 0
    # 시작 노드에서 갈 수 있는 노드에 대해 최단 경로 갱신
    for j in graph[start]:
        dist[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복 계산
    for _ in range(n - 1):
        # 방문하지 않은 노드 중 가장 최단거리의 인덱스를 꺼낸다
        now = get_smallest_node()
        visited[now] = True  # 방문 처리
        for j in graph[now]:
            cost = dist[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[j[0]] > cost:
                dist[j[0]] = cost  # 최단 거리 갱신

    # 다익스트라 알고리즘 수행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, n+1):
        # 도달할 수 없는 경우, INF으로 출력
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])
