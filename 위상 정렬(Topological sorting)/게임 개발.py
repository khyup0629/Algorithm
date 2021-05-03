# 위상 정렬 + DP
# 최소 시간이란 말에 잠깐 현혹됐었으나 먼저 지어져야하는 건물들이 모두 완료되어야
# 해당 건물을 지을 수 있기 때문에 해당 건물이 지어지는 시간은 최댓값이어야 한다.
from collections import deque
n = int(input())

dp = [0] * (n + 1)  # DP 테이블
delay = [0] * (n + 1)  # 시간 기록 테이블
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)  # 전입차수
for i in range(1, n+1):
    building = list(map(int, input().split()))
    delay[i] = building[0]
    for a in building[1:]:
        if a == -1:
            break
        graph[a].append(i)
        indegree[i] += 1


def topological_sorting():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i]

    while q:
        now = q.popleft()
        for x in graph[now]:
            indegree[x] -= 1
            dp[x] = max(dp[x], dp[now] + delay[x])
            if indegree[x] == 0:
                q.append(x)


topological_sorting()

for i in dp[1:]:
    print(i)

"""
문제
숌 회사에서 이번에 새로운 전략 시뮬레이션 게임 세준 크래프트를 개발하기로 하였다. 핵심적인 부분은 개발이 끝난 상태고, 
종족별 균형과 전체 게임 시간 등을 조절하는 부분만 남아 있었다.

게임 플레이에 들어가는 시간은 상황에 따라 다를 수 있기 때문에, 모든 건물을 짓는데 걸리는 최소의 시간을 이용하여 근사하기로 하였다. 
물론, 어떤 건물을 짓기 위해서 다른 건물을 먼저 지어야 할 수도 있기 때문에 문제가 단순하지만은 않을 수도 있다. 
예를 들면 스타크래프트에서 벙커를 짓기 위해서는 배럭을 먼저 지어야 하기 때문에, 배럭을 먼저 지은 뒤 벙커를 지어야 한다. 
여러 개의 건물을 동시에 지을 수 있다.

편의상 자원은 무한히 많이 가지고 있고, 건물을 짓는 명령을 내리기까지는 시간이 걸리지 않는다고 가정하자.

입력
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다. 다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과 그 건물을 짓기 위해 
먼저 지어져야 하는 건물들의 번호가 주어진다. 건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자. 
각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다.

출력
N개의 각 건물이 완성되기까지 걸리는 최소 시간을 출력한다.

예제 입력 1 
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
예제 출력 1 
10
20
14
18
17
"""