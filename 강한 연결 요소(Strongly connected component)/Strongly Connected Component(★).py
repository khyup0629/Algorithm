import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
reverseGraph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverseGraph[b].append(a)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)


def dfsReverse(x):
    temp.append(x)
    visited[x] = True
    for i in reverseGraph[x]:
        if not visited[i]:
            dfsReverse(i)


visited = [False] * (v + 1)
stack = []
for i in range(1, v+1):
    if not visited[i]:
        dfs(i)

visited = [False] * (v + 1)
scc = []
for _ in range(v):
    start = stack.pop()
    if not visited[start]:
        temp = []
        dfsReverse(start)
        temp.sort()
        scc.append(temp)

scc.sort()
print(len(scc))
for group in scc:
    print(*group, -1)

# 문제 : https://www.acmicpc.net/problem/2150
