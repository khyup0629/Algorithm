# 출력 형식을 어떻게 맞춰야 할지에 관해 해맨 문제
from collections import deque
import sys
sys.setrecursionlimit(10**5)   # 재귀 제한 해제

# n : 노드 개수 / m : 간선 개수 / v : 시작 노드
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]   # 그래프
for i in range(m):   # 그래프 그리기
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, n+1):   # 그래프 정렬
    graph[i].sort()

path_DFS = []   # DFS의 노드 탐색 순서
path_BFS = []   # BFS의 노드 탐색 순서


def dfs(x):   # DFS 함수
    visited[x] = True
    path_DFS.append(x)
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


def bfs(x):   # BFS 함수
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        start = q.popleft()
        path_BFS.append(start)
        for i in graph[start]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


visited = [False] * (n+1)   # 방문 여부 초기화
dfs(v)
visited = [False] * (n+1)   # 방문 여부 초기화
bfs(v)

print(' '.join(map(str, path_DFS)))
print(' '.join(map(str, path_BFS)))

# 문제 : https://www.acmicpc.net/problem/1260

"""
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
"""
