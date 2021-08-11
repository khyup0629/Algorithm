# 문제 풀이 아이디어(PyPy 제출)
# 1. 두 노드의 최소 공통 조상을 푸는 문제로 접근한다.
# 2. 부모 노드가 같아질 때까지 거슬러 올라가면서 간선의 비용을 모두 더하면 된다.
# 3. 임의로 루트 노드는 1로 해서 깊이와 부모 노드 테이블을 기록한다.
import sys
sys.setrecursionlimit(10**5)

n = int(input())

# 그래프에 연결되는 노드와 거리 정보를 같이 넣습니다.
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    node1, node2, cost = map(int, input().split())
    graph[node1].append([node2, cost])
    graph[node2].append([node1, cost])

depth = [0] * (n + 1)
parent = [0] * (n + 1)
visited = [False] * (n + 1)


def findDepthParent(x, d):  # 각 노드의 부모노드와 거리, 깊이를 계산합니다.
    visited[x] = True
    depth[x] = d
    for i, cost in graph[x]:
        if not visited[i]:
            parent[i] = (x, cost)
            findDepthParent(i, d+1)


def lca(a, b):
    dist = 0  # 두 노드의 거리
    # 두 매개변수 중 항상 b의 깊이가 더 깊도록 설정합니다.
    if depth[a] > depth[b]:
        a, b = b, a
    # 두 노드의 깊이가 같아질 때까지 거슬러 올라갑니다.
    while depth[a] != depth[b]:
        dist += parent[b][1]
        b = parent[b][0]
    # 같은 깊이에서 두 노드가 같아진다면 함수를 종료합니다.
    # 이 과정을 넣지 않으면 밑에 while문에서 인덱스 에러가 발생합니다.
    if a == b:
        return dist
    # 두 노드의 부모노드가 같아질 때까지 거슬러 올라갑니다.
    # 반복 종료 시점은 부모노드가 같을 때입니다.
    # 부모노드까지 거슬러올라가서 두 노드가 같아질 때까지가 아닙니다.
    while parent[a][0] != parent[b][0]:
        dist += (parent[a][1] + parent[b][1])
        a = parent[a][0]
        b = parent[b][0]
    # 부모 노드가 같으면 거슬러 올라가지 않고 반복을 종료했기 때문에 마지막 cost까지 더해주어야합니다.
    dist += (parent[a][1] + parent[b][1])
    return dist


findDepthParent(1, 0)  # 루트 노드를 항상 1로 놓고, 깊이는 0부터 시작합니다.

m = int(input())
for _ in range(m):
    node1, node2 = map(int, input().split())
    print(lca(node1, node2))


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
