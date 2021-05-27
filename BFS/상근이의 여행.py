# '가장 적은 종류' 라는 뜻은 a와 b를 왕복하는 비행기는 같은 종류를 의미한다는 뜻이다.
# 따라서, a -> b, b -> a로 두 번 이동해도 이용한 비행기는 한 종류이다.
# 이것을 바탕으로 문제를 해석해보면 모든 노드를 방문할 수 있는 최소 간선의 갯수를 구하는 문제가 된다.
# BFS 를 이용해 풀면 쉽게 풀 수 있다.

from collections import deque

t = int(input())


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visited[x]:
                visited[x] = True
                cnt += 1
                q.append(x)


for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    cnt = 0
    bfs(1)

    print(cnt)

# 문제 : https://www.acmicpc.net/problem/9372
