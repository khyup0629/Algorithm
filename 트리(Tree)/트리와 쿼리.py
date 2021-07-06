# 문제 풀이 아이디어
# 1. 각 노드마다 1의 값을 저장한다.
# 2. DFS 탐색을 통해 리프 노드부터 이전 노드의 값을 더하면서 거슬러 올라온다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
subtree = [1] * (n+1)
visited = [False] * (n+1)


def set_parent(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            set_parent(i)
            subtree[x] += subtree[i]


set_parent(r)
for _ in range(q):
    u = int(input())
    print(subtree[u])

# 문제 : https://www.acmicpc.net/problem/15681
