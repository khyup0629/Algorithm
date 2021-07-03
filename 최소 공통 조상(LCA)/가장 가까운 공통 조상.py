# 문제 풀이 아이디어
# 1. 입력값을 받을 때 각 노드의 연결 정보와 부모 노드 정보를 함께 기록한다.
# 2. 서로소 집합 알고리즘에서 썼던 find 함수를 이용해서 루트 노드를 찾는다.
# 3. 최소 공통 조상 알고리즘을 이용한다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())


def dfs(x, d):  # 루트 노드로부터 각 노드의 깊이 기록
    visited[x] = True
    depth[x] = d
    for i in graph[x]:
        if not visited[i]:
            dfs(i, d+1)


def lca(a, b):  # 최소 공통 조상 찾기
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[a] != depth[b]:
        b = parent[b]
    if a == b:
        return a
    while parent[a] != parent[b]:
        a = parent[a]
        b = parent[b]
    return parent[a]


def root(x):  # 루트 노드 찾기
    if parent[x] != x:
        return root(parent[x])
    return x


for _ in range(t):
    n = int(input())
    parent = [i for i in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a  # 부모 노드 기록
        graph[a].append(b)  # 부모 노드와 연결된 노드들 기록

    depth = [0] * (n+1)
    visited = [False] * (n+1)

    dfs(root(1), 0)  # 루트 노드로부터 각 노드까지의 깊이 기록
    d, e = map(int, input().split())

    print(lca(d, e))

# 문제 : https://www.acmicpc.net/problem/3584
