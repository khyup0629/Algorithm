import heapq
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    back_graph[b].append((a, c))


dist = [int(1e9)] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for x, cost in graph[now]:
            n_cost = cost + distance
            if dist[x] > n_cost:
                dist[x] = n_cost
                heapq.heappush(q, (n_cost, x))


def back(end):  # 최소비용을 기준으로 도착점에서부터 백트래킹하며 최단 경로를 찾는다.
    if end == start:
        return
    global _min
    for x, cost in back_graph[end]:
        if _min - cost == dist[x]:
            _min -= cost
            lst.append(x)
            back(x)
            break


start, end = map(int, input().split())
dijkstra(start)  # 시작점으로부터 모든 노드까지의 최소 비용 구하기
print(dist[end])  # 도착점의 최소 비용

lst = [end]  # 최단 경로가 담길 리스트. 도착점이 초기값으로 담겨있다.
_min = dist[end]
back(end)  # 도착점으로부터 시작점까지 백트래킹
print(len(lst))  # 최단 경로의 노드 개수

# lst 에는 도착점~시작점 순서로 기록되므로 거꾸로 출력한다.
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=' ')  # 시작점~도착점의 최단 경로

# 문제 : https://www.acmicpc.net/problem/11779
