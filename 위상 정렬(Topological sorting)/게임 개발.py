# 위상 정렬 + DP
# 최소 시간이란 말에 잠깐 현혹됐었으나 먼저 지어져야하는 건물들이 모두 완료되어야
# 해당 건물을 지을 수 있기 때문에 해당 건물이 지어지는 시간은 최댓값이어야 한다.
from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)  # 노드별 전입 차수
time = [0] * (n + 1)  # 노드별 건물을 짓는 시간
for i in range(1, n+1):
    building = list(map(int, input().split()))
    time[i] = building[0]
    for num in building[1:]:
        if num != -1:
            graph[num].append(i)
            indegree[i] += 1


def topological_sorting():  # 위상 정렬
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        for x in graph[now]:
            indegree[x] -= 1
            # x의 이전 노드들 중 가장 긴 시간을 dp[x]에 저장합니다.
            dp[x] = max(dp[x], time[now])
            if indegree[x] == 0:
                q.append(x)
                time[x] += dp[x]  # 전입차수가 0이 되었을 때 가장 긴 시간을 time에 더합니다.


dp = [0] * (n + 1)  # 이전 노드들 중 가장 긴 시간을 dp[x]에 저장합니다.
topological_sorting()
for t in time[1:]:
    print(t)

# 문제 : https://www.acmicpc.net/problem/1516
