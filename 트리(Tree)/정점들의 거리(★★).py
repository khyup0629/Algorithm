# 문제 풀이 아이디어(PyPy 제출)
# 1. 두 노드의 최소 공통 조상을 푸는 문제로 접근한다.
# 2. 부모 노드가 같아질 때까지 거슬러 올라가면서 간선의 비용을 모두 더하면 된다.
# 3. 임의로 루트 노드는 1로 해서 깊이와 부모 노드 테이블을 기록한다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

depth = [0] * (n + 1)
parent = [0] * (n + 1)
visited = [False] * (n + 1)


def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for i, cost in graph[x]:
        if not visited[i]:
            parent[i] = (x, cost)  # 올라갈 때의 간선의 비용도 함께 기록
            dfs(i, d+1)


def lca(a, b):
    global result
    if depth[a] > depth[b]:  # 항상 b의 깊이가 더 깊도록
        a, b = b, a
    while depth[a] != depth[b]:  # 둘의 깊이가 같아질 때까지
        result += parent[b][1]
        b = parent[b][0]
    if a == b:
        return
    # 같이 올라가기
    while parent[a][0] != parent[b][0]:
        result += parent[a][1] + parent[b][1]
        a = parent[a][0]
        b = parent[b][0]
    result += parent[a][1] + parent[b][1]


m = int(input())
dfs(1, 0)  # 임의로 루트 노드는 1
for _ in range(m):
    a, b = map(int, input().split())
    result = 0
    lca(a, b)
    print(result)


# 기존 DFS로 풀면 시간 초과(PyPy 제출 시 메모리 초과)
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def tree(x):
    global cost, result
    visited[x] = True
    if x == end:
        result = cost
        return
    for i, c in graph[x]:
        if not visited[i]:
            cost += c
            tree(i)
            cost -= c


m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n + 1)
    cost, result = 0, 0
    tree(start)
    print(result)

# 문제 : https://www.acmicpc.net/problem/1761
