# 위상정렬 + 백트래킹(휴리스틱)
# 지금까지 풀어왔던 백트래킹(DFS)과는 조금 다른 개념이었다.
# 1. 도착점부터 시작점까지 역으로 추적한다.
# 2. 현재 위치의 최대 비용에서 도로의 비용을 뺀 값이 다음 위치의 최대 비용과 같다면 큐에 추가하고 카운트 +1
#  이때, q에 중복되는 노드가 추가되는걸 방지하기 위해 방문 여부 리스트를 활용한다.
# 3. 2의 과정을 계속해서 반복한다.

from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]  # 위상 정렬을 위한 정방향 그래프
back_graph = [[] for _ in range(n+1)]  # 백트래킹을 위한 역방향 그래프
indegree = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    back_graph[b].append((a, c))
    indegree[b] += 1

start, end = map(int, input().split())

dp = [0] * (n+1)


def topological_sorting():
    # 위상 정렬
    global cnt
    q = deque()
    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for x, cost in graph[now]:
            indegree[x] -= 1
            dp[x] = max(dp[x], dp[now] + cost)
            if indegree[x] == 0:
                q.append(x)

    # 백트래킹(휴리스틱)
    visited = [False] * (n + 1)
    q.append(end)
    visited[end] = True
    while q:
        now = q.popleft()
        for x, cost in back_graph[now]:
            # 현재 위치의 최대 비용 - 도로의 비용 = 다음 위치의 최대비용이면,
            if dp[now] - cost == dp[x]:
                if not visited[x]:  # q에 중복으로 추가되는 것을 막아준다.
                    q.append(x)  # 방문을 하지 않았다면 방문 처리를 하고 한 번만 q에 추가해준다.
                    visited[x] = True
                cnt += 1  # 도로의 갯수 +1


cnt = 0
topological_sorting()

print(dp[end])
print(cnt)

# 문제 : https://www.acmicpc.net/problem/1948

"""
# 위상정렬 + DFS(백트래킹) : 시간 초과
from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[b] += 1

start, end = map(int, input().split())

dp = [0] * (n+1)


def topological_sorting():
    q = deque()
    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for x, cost in graph[now]:
            indegree[x] -= 1
            dp[x] = max(dp[x], dp[now] + cost)
            if indegree[x] == 0:
                q.append(x)


topological_sorting()
result = dp[end]
hap = 0
temp = []
result_cnt = []


def dfs(x):
    global hap, temp
    if x == end:
        if hap == result:
            result_cnt.extend(temp)
        return
    for i, cost in graph[x]:
        hap += cost
        temp.append((i, cost))
        dfs(i)
        # 백트래킹
        hap -= cost
        temp.pop()


dfs(start)

print(result)
print(len(set(result_cnt)))
"""