INF = int(1e9)

n, m = map(int, input().split())
# 2차원의 최단 거리 리스트를 만듦.
# 행 : 출발 노드, 열 : 도착 노드
graph = [[INF] * (n + 1) for _ in range(n+1)]
# 자기 자신에게로 향하는 최단 거리는 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 나머지 간선에 대한 최단 거리 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# a -> b와 a -> k -> b 를 고려
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
