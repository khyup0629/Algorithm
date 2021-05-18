from collections import deque
# 노드의 수, 줄의 수
n, m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    array = list(map(int, input().split()))
    for i in range(1, len(array)-1):
        graph[array[i]].append(array[i+1])
        indegree[array[i+1]] += 1


def topological_sorting():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)


result = []
topological_sorting()


if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)

# 문제 : https://www.acmicpc.net/problem/2623

"""
6 3
3 1 4 3
4 6 2 5 4
2 3 2
"""