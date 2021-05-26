# 트리 그래프를 베이스로 한 DFS + DP 문제이다.
# 트리의 지름 찾기 알고리즘
# 1. 1번 노드에서 가장 거리가 먼 노드(start)를 먼저 찾는다.
# 2. start 에서 DFS 탐색을 통해 가장 먼 거리(트리의 지름)를 찾는다.
import sys
sys.setrecursionlimit(10**5)

n = int(input())

dp = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    # 양방향 탐색이 가능하도록
    graph[a].append((b, c))
    graph[b].append((a, c))
    dp[b] = dp[a] + c  # 1번 노드에서 모든 노드까지의 거리를 DP 테이블에 기록

start = dp.index(max(dp))  # 가장 거리가 먼 노드의 번호를 기록


def dfs(x):  # start 에서 모든 노드까지의 거리를 DP 테이블에 담는다.
    for i, cost in graph[x]:
        if not visited[i]:
            visited[i] = True
            dp[i] = dp[x] + cost
            dfs(i)


dp = [0] * (n + 1)
visited = [False] * (n + 1)
visited[start] = True
dfs(start)  # DFS 탐색

print(max(dp))  # DP 테이블의 값 중 가장 큰 값이 트리의 지름

# 문제 : https://www.acmicpc.net/problem/1967
