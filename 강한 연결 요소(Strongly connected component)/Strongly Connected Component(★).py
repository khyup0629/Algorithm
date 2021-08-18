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

# 타잔 알고리즘 : id와 low의 초기값을 1e9로 주면 출력초과가 발생합니다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
cnt = -1
id = [-1] * (v + 1)
low = [-1] * (v + 1)
visited = [False] * (v+1)
stack = []


def dfs(x):
    global cnt
    cnt += 1
    low[x] = cnt
    id[x] = cnt
    stack.append(x)
    for i in graph[x]:
        if id[i] == -1:
            dfs(i)
        if not visited[i]:
            low[x] = min(low[x], low[i])
        print(low)

    popNode = -1  # stack에서 pop된 노드의 초기값
    scc = []  # 강한 연결 요소의 한 묶음
    if id[x] == low[x]:
        while popNode != x:
            popNode = stack.pop()
            scc.append(popNode)
            visited[popNode] = True
        result.append(sorted(scc))


result = []
for i in range(1, v+1):
    if id[i] == -1:
        dfs(i)

print(len(result))
for group in sorted(result):
    print(*group, -1)
