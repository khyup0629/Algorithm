# 위상 정렬을 수행하면 모든 노드를 탐색할 수 있다.
# 모든 노드를 탐색하면서 각 노드까지 작업을 끝낼 때 까지의 시간을 기록한 뒤
# 그 중에서 최댓값을 출력해주면 된다.
from collections import deque

n = int(input())

delay = [0]
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)  # 전입차수
for k in range(1, n+1):
    array = list(map(int, input().split()))
    delay.append(array[0])
    for i in range(array[1]):
        graph[array[i+2]].append(k)
        indegree[k] += 1
dp = [0] * (n+1)  # 현 노드까지 작업이 완료되기까지 걸리는 최대 시간이 기록될 장소


def topological_sorting():  # 위상 정렬
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i]

    while q:
        now = q.popleft()
        for x in graph[now]:
            indegree[x] -= 1
            dp[x] = max(dp[x], dp[now]+delay[x])
            if indegree[x] == 0:
                q.append(x)


topological_sorting()

print(max(dp))
