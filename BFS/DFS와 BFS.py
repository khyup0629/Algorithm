# 출력 형식을 어떻게 맞춰야 할지에 관해 해맨 문제
from collections import deque

import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제

# n : 정점의 개수, m : 간선의 개수, v : 시작 번호
n, m, v = map(int, input().split(' '))
# 각 인덱스와 연결되는 다른 정점들을 표시
pair = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split(' '))
    pair[start].append(end)
    pair[end].append(start)
# 각 칸 당 노드 번호 정렬(작은 값부터 방문해야하기 때문)
for i in range(n+1):
    pair[i].sort()

# dfs 와 bfs 의 경로를 기록하기 위한 빈 리스트
path_dfs = []
path_bfs = []


def dfs(x):
    visited[x] = True
    # dfs 의 경로 기록
    path_dfs.append(x)
    for number in pair[x]:
        if not visited[number]:
            visited[number] = True
            dfs(number)


def bfs(x):
    visited[x] = True
    q = deque()
    # bfs 의 최초 경로만 기록
    q.append(x)
    path_bfs.append(x)
    while q:
        z = q.popleft()
        for number in pair[z]:
            if not visited[number]:
                visited[number] = True
                # bfs 의 나머지 경로 기록
                path_bfs.append(number)
                q.append(number)


# 방문/미방문 여부 초기화
visited = [False] * (n + 1)
dfs(v)
# 리스트 요소를 한 칸씩 띄워서 출력하고 줄을 바꿔서
# 다른 리스트 요소를 한 칸씩 띄워서 출력하고 싶다면
print(' '.join(map(str, path_dfs)))
# 방문/미방문 여부 초기화
visited = [False] * (n + 1)
bfs(v)
print(' '.join(map(str, path_bfs)))

"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
"""
