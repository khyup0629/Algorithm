# 입력값의 범위가 크기 때문에, 희소 배열을 이용해서 시간 복잡도를 줄여야 한다.
# 문제 풀이 아이디어
# 1. 부모 노드를 희소 테이블로 둔다. 이때, 기존에 2차원으로 두는 것이 아닌, 3차원으로 두어
# [부모 노드 번호, 가장 작은 경로, 가장 큰 경로]의 형식으로 저장할 수 있도록 한다.
# 2. j번 노드의 2^i 번째 부모 노드의 값들을 구할 때(set_parent) 가장 작은 경로와 큰 경로를 갱신한다.
# 3. 노드를 거슬러 올라갈 때마다 최소 경로, 최대 경로를 갱신한다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

LOG = 21
depth = [0] * (n + 1)
parent = [[[0, 0, 0] for _ in range(LOG)] for _ in range(n+1)]
visited = [False] * (n + 1)


def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for i, cost in graph[x]:
        if not visited[i]:
            parent[i][0][0] = x
            parent[i][0][1] = cost
            parent[i][0][2] = cost
            dfs(i, d+1)


def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i][0] = parent[parent[j][i - 1][0]][i - 1][0]
            # 0~i-1 번째까지의 최소, 최댓값과 i-1~i까지의 최소, 최댓값 중 최소, 최댓값을 구한다.
            parent[j][i][1] = min(parent[j][i - 1][1], parent[parent[j][i - 1][0]][i - 1][1])
            parent[j][i][2] = max(parent[j][i - 1][2], parent[parent[j][i - 1][0]][i - 1][2])


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    shortest = int(10**9)
    longest = 0
    for i in range(LOG-1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            shortest = min(shortest, parent[b][i][1])
            longest = max(longest, parent[b][i][2])
            b = parent[b][i][0]
    if a == b:
        return shortest, longest
    for i in range(LOG-1, -1, -1):
        if parent[a][i][0] != parent[b][i][0]:
            shortest = min(shortest, parent[a][i][1], parent[b][i][1])
            longest = max(longest, parent[a][i][2], parent[b][i][2])
            a = parent[a][i][0]
            b = parent[b][i][0]
    shortest = min(shortest, parent[a][0][1], parent[b][0][1])
    longest = max(longest, parent[a][0][2], parent[b][0][2])
    return shortest, longest


k = int(input())
set_parent()
for _ in range(k):
    d, e = map(int, input().split())
    shortest, longest = lca(d, e)
    print(shortest, longest)

# 문제 : https://www.acmicpc.net/problem/3176
