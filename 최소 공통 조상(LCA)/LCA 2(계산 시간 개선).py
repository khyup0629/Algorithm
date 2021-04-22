# 시간 복잡도 : O(MlogN), 시간 복잡도 개선

import sys
# 시간 초과를 피하기 위한 빠른 입력
input = sys.stdin.readline
sys.setrecursionlimit(100000)
LOG = 21  # 2^20 = 1,000,000

n = int(input())
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
            visited[i] = True
            parent[i][0] = x
            dfs(i, d + 1)


def set_parent():  # 2^i 만큼 거슬러 올라갔을 때의 부모 노드 번호를 기록
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
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

"""
문제
N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

예제 입력 1 
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15
예제 출력 1 
2
4
2
1
3
1
"""
