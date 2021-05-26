# 트리의 지름 찾기 알고리즘
# 1. 임의의 노드에서 가장 거리가 먼 노드(start)를 먼저 찾는다.
# 2. start 에서 DFS 탐색을 통해 가장 먼 거리(트리의 지름)를 찾는다.
import sys
sys.setrecursionlimit(10**5)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        if i % 2 == 1:
            graph[arr[0]].append((arr[i], arr[i+1]))


def dfs(x):  # x에서 각 노드까지의 거리를 DP 테이블에 기록한다.
    for i, cost in graph[x]:
        if not visited[i]:
            visited[i] = True
            dp[i] = dp[x] + cost
            dfs(i)


# 임의의 한 노드(1)에서 가장 먼 거리에 위치한 노드(start)를 찾는다.
dp = [0] * (n + 1)  # 초기화
visited = [False] * (n + 1)  # 초기화
visited[1] = True
dfs(1)

start = dp.index(max(dp))  # 1번 노드에서 가장 먼 거리에 있는 노드

# start 에서 가장 먼 거리를 출력한다.
dp = [0] * (n + 1)  # 초기화
visited = [False] * (n + 1)  # 초기화
visited[start] = True
dfs(start)

print(max(dp))  # start 에서 가장 먼 거리

# 문제 : https://www.acmicpc.net/problem/1167
# 유사 문제 : https://www.acmicpc.net/problem/1967
