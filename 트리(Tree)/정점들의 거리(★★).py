# 기존 DFS로 풀면 시간 초과.
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
