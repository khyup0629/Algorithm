# 서로소 집합 또는 BFS로 풀 수 있다.

import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, computers):
    answer = 0

    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        parent[b] = a

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(i, j)

    for i in range(n):
        if parent[i] == i:
            answer += 1

    return answer


# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43162#

"""
from collections import deque


def solution(n, computers):
    answer = 0

    visited = [False] * n  # 방문 체크

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            now = q.popleft()
            for x in graph[now]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43162#
"""