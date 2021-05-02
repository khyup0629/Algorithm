# 위상정렬 + DP가 혼합된 문제
# 위상 정렬에 따라 노드를 탐색하면서 DP 테이블에 최댓값을 갱신한다.

from collections import deque
t = int(input())


def topological_sorting():
    q = deque()
    # 전입차수 = 0인 인덱스를 q에 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    while q:
        now = q.popleft()
        for k in graph[now]:
            indegree[k] -= 1
            dp[k] = max(dp[k], dp[now] + cost[k])
            if indegree[k] == 0:
                q.append(k)


for _ in range(t):
    # 건물의 개수, 간선의 개수
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)  # 전입차수
    dp = [0] * (n + 1)  # DP 테이블 초기화
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())  # 도착지점

    topological_sorting()

    print(dp[w])

"""

"""