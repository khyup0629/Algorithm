# 시간 복잡도 : O(NM)
import sys
sys.setrecursionlimit(100000)

# 노드의 개수
n = int(input())

parent = [0] * (n + 1)  # 부모 노드 정보
depth = [0] * (n + 1)  # 깊이 정보
visited = [False] * (n + 1)  # 방문 여부 정보
# 그래프 정보
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(x, d):  # (현재 노드, 깊이)
    visited[x] = True
    depth[x] = d
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            parent[i] = x
            dfs(i, d + 1)  # 재귀 함수


def lca(a, b):
    while depth[a] != depth[b]:  # 깊이가 같아질 때까지
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:  # 부모 노드가 같아질 때까지
        a = parent[a]
        b = parent[b]
    return a


# DFS 로 각 노드까지의 깊이와 부모 노드 구하기
dfs(1, 0)  # 루트 노드는 1이고 깊이는 0
# 최소 공통 조상을 찾고 싶은 개수
m = int(input())
# 최소 공통 조상 수행
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
