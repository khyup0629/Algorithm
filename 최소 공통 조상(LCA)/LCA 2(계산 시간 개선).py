# 시간 복잡도 : O(MlogN), 시간 복잡도 개선

import sys
# 시간 초과를 피하기 위한 빠른 입력
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# 데이터가 최대 1,000,000개 들어올 수 있다고 가정.
LOG = 21  # 2^20 = 1,000,000

n = int(input())
# parent[j][i] : j번 노드의 2^i 위의 부모 노드
parent = [[0] * LOG for _ in range(n + 1)]
depth = [0] * (n + 1)
visited = [False] * (n + 1)

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for i in graph[x]:
        if not visited[i]:
            parent[i][0] = x  # 바로 위의 2^0 부모 노드들을 기록.
            dfs(i, d + 1)


def set_parent():  # 2^i 만큼 거슬러 올라갔을 때의 부모 노드 번호를 기록
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            # j번 노드의 2^i 부모 노드는 j번 노드의 2^i-1 의 부모 노드의 2^i-1 거슬러 올라간 부모 노드와 같다.
            parent[j][i] = parent[parent[j][i-1]][i-1]


def lca(a, b):
    # b의 깊이가 a보다 항상 더 깊어야 한다
    if depth[a] > depth[b]:
        a, b = b, a
    # 깊이가 같아질 때까지 b를 2^i 씩 끌어올림.
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:  # 위의 과정에서 a와 b가 같아지면 종료
        return a
    # a와 b의 깊이를 2^i 씩 끌어올리면서
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

# 문제 : https://www.acmicpc.net/problem/11438
